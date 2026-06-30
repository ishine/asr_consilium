## Datasets

Three datasets were used for testing:
* [FLEURS](https://huggingface.co/datasets/google/fleurs)
* [MCV](https://huggingface.co/datasets/facebook/covost2)
* [MLS](https://www.openslr.org/94)

They all were gathered in [one big ASR testing dataset](https://huggingface.co/datasets/nithinraok/asr-leaderboard-datasets).

## French Language

### WER

| Model name                | avg  | fleurs_fr | mls_fr | mcv_fr |
|--------------------------------------------------------------------------------------|------|-----------|---------|--------|
| [Nvidia Parakeet v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3)             | 5.38 | 5.16          |   4.93      |  6.05      |
| [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B)                         | 5.80 | 4.44          |  4.96       |  8.02      |
| [IBM Granite Speech 4.0-1B](https://huggingface.co/ibm-granite/granite-4.0-1b-speech) | 6.23 |   8.32         |    4.27      |  6.10      |
| [IBM Granite Speech 3.3-8B](https://huggingface.co/ibm-granite/granite-speech-3.3-8b) | 5.74 |  7.43         |  3.93       |   5.87     |
| [Granite-Speech-4.1-2B](https://huggingface.co/ibm-granite/granite-speech-4.1-2b)    | 5.67 |  7.60         |  4.10       |  5.32      |
| [Microsoft-Phi-4](https://huggingface.co/microsoft/Phi-4-multimodal-instruct)        | 5.07 |    4.61       |  4.12       |   6.50     |
| [Voxtral-Mini-3B-2507](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507)        | 5.71 |  4.64         |   5.08      |  7.41      |
| Ensemble (Default parameters)    | 3.47 |  3.56         |  2.66       |  4.19      |

## German Language

### WER

| Model name | avg | fleurs_de | mcv_de |
| --- | --- | --- | --- |
| [Nvidia Parakeet v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) | 4.92 | 5.05 | 4.80 |
| [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | 4.91 | 4.11 | 5.71 |
| [IBM Granite Speech 4.0-1B](https://huggingface.co/ibm-granite/granite-4.0-1b-speech) | 5.72 | 7.09 | 4.36 |
| [IBM Granite Speech 3.3-8B](https://huggingface.co/ibm-granite/granite-speech-3.3-8b) | 5.25 | 6.34 | 4.16 |
| [Granite-Speech-4.1-2B](https://huggingface.co/ibm-granite/granite-speech-4.1-2b) | 4.69 | 5.96 | 3.41 |
| [ZFTurbo-Phi-4](https://www.google.com/search?q=https://huggingface.co/ZFTurbo/Phi-4-multimodal-instruct) | 4.51 | 4.39 | 4.62 |
| [Voxtral-Mini-3B-2507](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507) | 5.32 | 4.58 | 6.07 |
| Ensemble (Default parameters) | 2.88 | 3.14 | 2.62 |

### CER

| Model name | avg | fleurs_de | mcv_de |
| --- | --- | --- | --- |
| [Nvidia Parakeet v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) | 1.37 | 1.49 | 1.25 |
| [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | 1.61 | 1.35 | 1.88 |
| [IBM Granite Speech 4.0-1B](https://huggingface.co/ibm-granite/granite-4.0-1b-speech) | 2.58 | 3.82 | 1.33 |
| [IBM Granite Speech 3.3-8B](https://huggingface.co/ibm-granite/granite-speech-3.3-8b) | 2.57 | 3.79 | 1.35 |
| [Granite-Speech-4.1-2B](https://huggingface.co/ibm-granite/granite-speech-4.1-2b) | 2.31 | 3.65 | 0.96 |
| [ZFTurbo-Phi-4](https://www.google.com/search?q=https://huggingface.co/ZFTurbo/Phi-4-multimodal-instruct) | 1.69 | 1.73 | 1.64 |
| [Voxtral-Mini-3B-2507](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507) | 1.94 | 1.74 | 2.14 |
| Ensemble (Default parameters) | 1.04 | 1.23 | 0.84 |

## Italian language

### WER

| Model name | avg | fleurs_it | mls_it | mcv_it |
| --- | --- | --- | --- | --- |
| [Nvidia Parakeet v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) | 5.58 | 2.96 | 10.12 | 3.65 |
| [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | 6.27 | 2.56 | 11.27 | 5.00 |
| [Granite-Speech-4.1-2B](https://huggingface.co/ibm-granite/granite-speech-4.1-2b) | 7.95 | 6.66 | 10.45 | 6.75 |
| [ZFTurbo-Phi-4](https://www.google.com/search?q=https://huggingface.co/ZFTurbo/Phi-4-multimodal-instruct) | 4.75 | 2.36 | 8.48 | 3.42 |
| [Voxtral-Mini-3B-2507](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507) | 5.73 | 2.51 | 9.38 | 5.30 |
| Ensemble (Default parameters) | 3.74 | 1.80 | 6.87 | 2.56 |

## CER

| Model name | avg | fleurs_it | mls_it | mcv_it |
| --- | --- | --- | --- | --- |
| [Nvidia Parakeet v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) | 1.40 | 0.97 | 2.26 | 0.98 |
| [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | 1.69 | 0.95 | 2.61 | 1.52 |
| [Granite-Speech-4.1-2B](https://huggingface.co/ibm-granite/granite-speech-4.1-2b) | 2.94 | 3.73 | 3.01 | 2.08 |
| [ZFTurbo-Phi-4](https://www.google.com/search?q=https://huggingface.co/ZFTurbo/Phi-4-multimodal-instruct) | 1.45 | 1.10 | 2.19 | 1.06 |
| [Voxtral-Mini-3B-2507](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507) | 1.69 | 1.17 | 2.19 | 1.72 |
| Ensemble (Default parameters) | 1.11 | 0.70 | 1.80 | 0.82 |

## Spanish language

### WER

| Model name | avg | fleurs_es | mls_es | mcv_es |
| --- | --- | --- | --- | --- |
| [Nvidia Parakeet v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) | 3.72 | 3.48 | 4.29 | 3.41 |
| [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | 3.80 | 3.14 | 4.28 | 3.98 |
| [IBM Granite Speech 4.0-1B](https://huggingface.co/ibm-granite/granite-4.0-1b-speech) | 4.36 | 5.54 | 3.53 | 4.00 |
| [IBM Granite Speech 3.3-8B](https://huggingface.co/ibm-granite/granite-speech-3.3-8b) | 4.22 | 5.16 | 3.63 | 3.89 |
| [Granite-Speech-4.1-2B](https://huggingface.co/ibm-granite/granite-speech-4.1-2b) | 3.90 | 5.23 | 3.15 | 3.33 |
| [ZFTurbo-Phi-4](https://www.google.com/search?q=https://huggingface.co/ZFTurbo/Phi-4-multimodal-instruct) | 3.56 | 3.20 | 3.70 | 3.77 |
| [Voxtral-Mini-3B-2507](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507) | 3.76 | 3.38 | 3.88 | 4.04 |
| Ensemble (Default parameters) | 2.42 | 2.34 | 2.65 | 2.28 |

### CER

| Model name | avg | fleurs_es | mls_es | mcv_es |
| --- | --- | --- | --- | --- |
| [Nvidia Parakeet v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) | 1.29 | 1.35 | 1.43 | 1.09 |
| [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | 1.38 | 1.37 | 1.41 | 1.38 |
| [IBM Granite Speech 4.0-1B](https://huggingface.co/ibm-granite/granite-4.0-1b-speech) | 1.93 | 3.12 | 1.22 | 1.45 |
| [IBM Granite Speech 3.3-8B](https://huggingface.co/ibm-granite/granite-speech-3.3-8b) | 1.95 | 3.09 | 1.28 | 1.47 |
| [Granite-Speech-4.1-2B](https://huggingface.co/ibm-granite/granite-speech-4.1-2b) | 1.79 | 3.08 | 1.14 | 1.15 |
| [ZFTurbo-Phi-4](https://www.google.com/search?q=https://huggingface.co/ZFTurbo/Phi-4-multimodal-instruct) | 1.42 | 1.54 | 1.26 | 1.45 |
| [Voxtral-Mini-3B-2507](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507) | 1.54 | 1.76 | 1.33 | 1.53 |
| Ensemble (Default parameters) | 0.94 | 1.08 | 0.94 | 0.81 |

## Portuguese language

### WER

| Model name | avg | fleurs_pt | mls_pt | mcv_pt |
| --- | --- | --- | --- | --- |
| [Nvidia Parakeet v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) | 5.26 | 4.79 | 7.19 | 3.80 |
| [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | 5.43 | 4.22 | 8.10 | 3.97 |
| [IBM Granite Speech 4.0-1B](https://huggingface.co/ibm-granite/granite-4.0-1b-speech) | 8.21 | 8.96 | 14.78 | 0.90 |
| [IBM Granite Speech 3.3-8B](https://huggingface.co/ibm-granite/granite-speech-3.3-8b) | 6.27 | 7.92 | 9.85 | 1.04 |
| [Granite-Speech-4.1-2B](https://huggingface.co/ibm-granite/granite-speech-4.1-2b) | 7.16 | 9.30 | 11.34 | 0.85 |
| [ZFTurbo-Phi-4](https://www.google.com/search?q=https://huggingface.co/ZFTurbo/Phi-4-multimodal-instruct) | 4.51 | 4.25 | 6.37 | 2.91 |
| [Voxtral-Mini-3B-2507](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507) | 4.48 | 3.74 | 5.69 | 4.00 |
| Ensemble (Default parameters) | 2.74 | 3.20 | 3.84 | 1.19 |

### CER

| Model name | avg | fleurs_pt | mls_pt | mcv_pt |
| --- | --- | --- | --- | --- |
| [Nvidia Parakeet v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) | 2.06 | 1.92 | 2.90 | 1.35 |
| [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | 2.07 | 1.77 | 3.00 | 1.44 |
| [IBM Granite Speech 4.0-1B](https://huggingface.co/ibm-granite/granite-4.0-1b-speech) | 3.76 | 4.67 | 6.22 | 0.40 |
| [IBM Granite Speech 3.3-8B](https://huggingface.co/ibm-granite/granite-speech-3.3-8b) | 2.76 | 4.33 | 3.52 | 0.44 |
| [Granite-Speech-4.1-2B](https://huggingface.co/ibm-granite/granite-speech-4.1-2b) | 2.88 | 4.84 | 3.45 | 0.35 |
| [ZFTurbo-Phi-4](https://www.google.com/search?q=https://huggingface.co/ZFTurbo/Phi-4-multimodal-instruct) | 1.74 | 1.73 | 2.35 | 1.13 |
| [Voxtral-Mini-3B-2507](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507) | 1.80 | 1.68 | 2.13 | 1.60 |
| Ensemble (Default parameters) | 1.13 | 1.37 | 1.55 | 0.46 |

## Russian language

### WER

| Model name | avg  | fleurs_ru | mcv_ru |
| --- |------|-----------|--------|
| [Nvidia Parakeet v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) | 4.25 | 5.54      | 2.97   |
| [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | 5.19 | 5.34      | 5.05   |
| [Voxtral-Mini-3B-2507](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507) | 7.72 | 8.34      | 7.11   |
| [Whisper Large v3](https://huggingface.co/openai/whisper-large-v3) | 3.69 | 3.77      | 3.62   |
| Ensemble (Default parameters) | 2.99 | 3.67      | 2.31   |

### CER

| Model name | avg  | fleurs_ru | mcv_ru |
| --- |------|-----------|--------|
| [Nvidia Parakeet v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) | 1.15 | 1.59      | 0.71   |
| [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | 1.73 | 1.79      | 1.66   |
| [Voxtral-Mini-3B-2507](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507) | 3.09 | 3.42      | 2.76   |
| [Whisper Large v3](https://huggingface.co/openai/whisper-large-v3) | 1.18 | 1.14      | 1.22   |
| Ensemble (Default parameters) | 0.88 | 1.15      | 0.60   |