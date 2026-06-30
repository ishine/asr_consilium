import os
import torch
import time
from tqdm import tqdm
import json
import librosa
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor
from .utils import get_dynamic_batches, store_results

ISO_TO_LANGUAGE_MAP = {
    "zh": "chinese", "en": "english", "ar": "arabic", "de": "german",
    "fr": "french", "es": "spanish", "pt": "portuguese", "id": "indonesian",
    "it": "italian", "ko": "korean", "ru": "russian", "th": "thai",
    "vi": "vietnamese", "ja": "japanese", "tr": "turkish", "hi": "hindi",
    "ms": "malay", "nl": "dutch", "sv": "swedish", "da": "danish",
    "fi": "finnish", "pl": "polish", "cs": "czech", "tl": "filipino",
    "fa": "persian", "el": "greek", "ro": "romanian", "hu": "hungarian",
    "mk": "macedonian"
}


def proc_data_with_whisper(
        jsonl_file,
        out_file,
        batch_size=16,
        language='en',
        model_path="openai/whisper-large-v3",
):
    """
    :param jsonl_file: path to the data file
    :param out_file: path to save the output
    :param batch_size: batch size
    :param language: language
    :param model_path: path to the Whisper model
    :return: dict with predictions. Choose from:
       openai/whisper-large-v3
       openai/whisper-large-v2
       openai/whisper-large
       openai/whisper-medium
       openai/whisper-small
       openai/whisper-base
       openai/whisper-tiny
    """

    device = "cuda" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
    print(f"Loading model: {model_path} Language: {language}")

    # Load the processor and model
    processor = AutoProcessor.from_pretrained(model_path)
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_path,
        torch_dtype=torch_dtype,
        low_cpu_mem_usage=True,
        use_safetensors=True
    ).to(device)

    # Prepare the data
    lines = open(jsonl_file, 'r', encoding="utf-8").readlines()
    items = [json.loads(line) for line in lines]

    # Sorting by duration is crucial for efficient padding within batches
    items.sort(key=lambda x: x.get("duration", 0), reverse=True)
    abs_path = os.path.dirname(jsonl_file)

    gen_kwargs = {
        "max_new_tokens": 428,
        "return_timestamps": False,
    }

    if language is not None and language in ISO_TO_LANGUAGE_MAP:
        gen_kwargs['language'] = ISO_TO_LANGUAGE_MAP[language]

    start_time_overall = time.time()
    cur_time = time.time()
    predictions = {}

    print("Starting inference...")

    with torch.inference_mode():
        with tqdm(total=len(items), desc="Processing audio") as pbar:
            for batch in get_dynamic_batches(items, batch_size):
                batch_audios = []
                item_chunk_counts = []

                for item in batch:
                    path = os.path.join(abs_path, str(item["audio"]))
                    audio, _ = librosa.load(path, sr=16000, mono=True)
                    max_samples = 16000 * 30
                    chunks = [audio[i:i + max_samples] for i in range(0, len(audio), max_samples)]
                    batch_audios.extend(chunks)
                    item_chunk_counts.append(len(chunks))

                inputs = processor(
                    batch_audios,
                    sampling_rate=16000,
                    return_tensors="pt",
                    truncation=False,
                    padding="longest",
                    return_attention_mask=True,
                )
                inputs = inputs.to(device, dtype=torch_dtype)

                pbar.update(len(batch))
                pbar.set_postfix({
                    "batch items": len(batch),
                    "total chunks": len(batch_audios),
                    "iter time (sec)": round(time.time() - cur_time, 2),
                })
                cur_time = time.time()

                output_ids = model.generate(
                    **inputs,
                    **gen_kwargs
                )

                decoded_preds = processor.batch_decode(
                    output_ids,
                    skip_special_tokens=True,
                    decode_with_timestamps=False
                )

                pred_idx = 0
                for item, num_chunks in zip(batch, item_chunk_counts):
                    full_text = " ".join(decoded_preds[pred_idx: pred_idx + num_chunks])
                    predictions[item['audio']] = full_text.strip()
                    pred_idx += num_chunks

    print("Transcription complete in {:.2f} seconds".format(time.time() - start_time_overall))

    if out_file is not None:
        store_results(predictions, out_file)

    return predictions