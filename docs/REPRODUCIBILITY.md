# Reproducibility Guide

## Scope

The notebooks are designed primarily for Kaggle's competition runtime. Full local execution is not guaranteed because the model, metric utility, CUDA kernels, and package wheels are environment-specific.

## A. Continued LoRA training

Open:

```text
notebooks/01_replay_math_continued_training.ipynb
```

### Required inputs

1. NVIDIA Nemotron competition data.
2. Huikang tokenized SFT snapshot and `index.jsonl`.
3. Replay Math JSONL.
4. A previous compatible LoRA adapter packaged as `submission.zip`.
5. Offline package wheels referenced in the configuration cell.
6. Optional OpenMathReasoning JSONL when `USE_OPENMATH=True`.

### Default adapter assumptions

- PEFT LoRA adapter.
- Rank 32.
- Target modules compatible with the notebook configuration.
- Adapter archive contains `adapter_config.json` and either `adapter_model.safetensors` or `adapter_model.bin`.

### Key switches

```python
NUM_STEPS = 400
LEARNING_RATE = 1e-5
REPLAY_FINAL_RATIO = 0.10
USE_OPENMATH = False
OPENMATH_FINAL_RATIO = 0.0
PRETRAINED_ADAPTER_ZIP = "AUTO"
```

Set `PRETRAINED_ADAPTER_ZIP` to an exact path when automatic discovery finds multiple ambiguous archives.

### Expected output

```text
/kaggle/working/submission.zip
```

The archive should contain only the adapter artifacts, normally:

```text
adapter_config.json
adapter_model.safetensors
```

## B. Local validation and dashboard

Open:

```text
notebooks/02_local_cv_and_dashboard.ipynb
```

### Required inputs

1. A compatible `submission.zip` or extracted adapter directory.
2. `val_set_950.jsonl` with at least `id`, `prompt`, and `answer` columns; `label` is recommended.
3. The official Kaggle metric utility available in the runtime.

### Recommended first run

Use smoke-test mode before the full 950-example evaluation:

```python
CFG['SMOKE_TEST'] = True
CFG['SMOKE_N'] = 50
```

Then switch back to:

```python
CFG['SMOKE_TEST'] = False
```

### Main inference parameters

```python
MAX_LORA_RANK = 32
MAX_TOKENS = 7680
TEMPERATURE = 0.0
TOP_P = 1.0
MAX_NUM_SEQS = 64
GPU_MEMORY_UTILIZATION = 0.85
MAX_MODEL_LEN = 8192
```

### Expected outputs

```text
debug_predictions.csv
analysis_outputs/overall_summary.csv
analysis_outputs/per_label_metrics.csv
analysis_outputs/wrong_cases.csv
analysis_outputs/missing_extraction_cases.csv
analysis_outputs/local_cv_report.md
figures/*.png
submission.zip
```

The advanced dashboard can additionally consume multi-version results, training-mixture tables, and self-consistency result files through the optional configuration lists.

## C. Repository validation

The included validator checks that both notebooks are valid `nbformat` documents and that all code cells parse as Python:

```bash
python -m pip install -r requirements.txt
python scripts/validate_notebooks.py
```

This check deliberately avoids executing model training or inference.
