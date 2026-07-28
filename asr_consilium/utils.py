import os
from tqdm import tqdm
import soundfile as sf
import json


def get_dynamic_batches(
    items,
    batch_size=16
):
    total = len(items)
    i = 0
    while i < total:
        yield items[i: i + batch_size]
        i += batch_size


def get_dynamic_batches_advanced(
    items,
    available_mem=16
):
    """
    Get batches
    :param items:
    :param available_mem: your GPU VRAM size in GB
    :return:
    """

    MAX_BATCH_SIZE = 256
    total = len(items)
    i = 0

    while i < total:
        if items[i]['duration'] > 200:
            batch_size = 1
        else:
            batch_size = int(20 * available_mem / items[i]['duration']) + 1
            if batch_size > MAX_BATCH_SIZE:
                batch_size = MAX_BATCH_SIZE

        yield items[i: i + batch_size]
        i += batch_size


def store_results(results, output_file):
    out = open(output_file, "w", encoding='utf-8')
    for audio, text in results.items():
        r = {"audio": audio, "text": text}
        out.write(json.dumps(r, ensure_ascii=False) + '\n')
    out.close()


def store_test_dataset_as_files(dataset, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    output_jsonl_file = os.path.join(out_dir, "markdown.jsonl")
    if os.path.isfile(output_jsonl_file):
        print("Dataset already created!")
        return output_jsonl_file
    out = open(output_jsonl_file, 'w', encoding='utf-8')
    print("Dataset length: {}".format(len(dataset['test'])))
    for i in tqdm(range(len(dataset['test']))):
        orig_name = dataset['test'][i]["audio"]["path"]
        audio = dataset['test'][i]["audio"]["array"]
        sr = dataset['test'][i]["audio"]["sampling_rate"]
        sf.write(os.path.join(out_dir, orig_name), audio, sr, 'FLOAT')
        res = {
            'audio': orig_name,
            'text': dataset['test'][i]['text'],
            'duration': len(audio) / sr,
        }
        out.write(json.dumps(res, ensure_ascii=False) + '\n')
    out.close()
    return output_jsonl_file


def store_test_dataset_as_files_unique(dataset, out_dir, name='test'):
    os.makedirs(out_dir, exist_ok=True)
    output_jsonl_file = os.path.join(out_dir, "markdown.jsonl")
    if os.path.isfile(output_jsonl_file):
        print("Dataset already created!")
        return output_jsonl_file
    out = open(output_jsonl_file, 'w', encoding='utf-8')
    print(dataset)
    print("Dataset length: {}".format(len(dataset[name])))
    for i in tqdm(range(len(dataset[name]))):
        # print(dataset[name][i])
        if dataset[name][i]["audio"]["path"] is None:
            orig_name = '{}.wav'.format(i)
        else:
            part = dataset[name][i]["audio"]["path"][:-4]
            part = part.replace(":", "")
            orig_name = os.path.basename(part + '_{}.wav'.format(i))
        audio = dataset[name][i]["audio"]["array"]
        sr = dataset[name][i]["audio"]["sampling_rate"]
        # print(out_dir, orig_name, os.path.join(os.path.abspath(out_dir), orig_name))
        sf.write(os.path.join(out_dir, orig_name), audio, sr, 'FLOAT')
        res = {
            'audio': orig_name,
            'text': dataset[name][i]['text'],
            'duration': len(audio) / sr,
        }
        out.write(json.dumps(res, ensure_ascii=False) + '\n')
    out.close()
    return output_jsonl_file

