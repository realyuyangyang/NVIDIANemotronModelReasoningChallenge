# Dataset Notes

No dataset is stored in this repository. The notebooks expect external Kaggle inputs.

## Huikang rule-induced SFT

Used as the primary task-alignment corpus. It provides competition-style prompts and supervised reasoning traces organized as a tokenized SFT snapshot plus a training-order index.

Notebook paths:

```text
/kaggle/input/datasets/huikang/huikang-nemotron-repository-snapshot/
  nemotron-master/training/sft/04-08-16-14/tokens
/kaggle/input/datasets/huikang/huikang-nemotron-repository-snapshot/
  nemotron-master/training/sft/04-08-16-14/logprobs/index.jsonl
```

## Nemotron Math / Replay Math

Used to strengthen general mathematical reasoning and reduce over-specialization to the competition task format.

Notebook path:

```text
/kaggle/input/datasets/mohamedamr992/replay-math/nemotron_math_1gb.jsonl
```

The continuation notebook tokenizes message-format records with the base-model chat template and samples examples to a target final mixture ratio.

## OpenMathReasoning

Used in the broader progressive solution as a later low-learning-rate continuation source. The notebook can discover `train_reasoning.jsonl` automatically when `USE_OPENMATH=True` and the corresponding notebook output or dataset is attached.

## Competition data

The training notebook reads:

```text
/kaggle/input/competitions/nvidia-nemotron-model-reasoning-challenge/train.csv
```

The local-CV notebook expects a validation file named:

```text
val_set_950.jsonl
```

## Model and package artifacts

The base model is downloaded through KaggleHub using:

```text
metric/nemotron-3-nano-30b-a3b-bf16/transformers/default
```

The training notebook also expects Kaggle-compatible offline wheels for Unsloth, Mamba SSM, causal-conv1d, and related dependencies. These binary artifacts are not included here.

## License responsibility

Each dataset, model, competition file, and wheel remains governed by its original license and terms. Users are responsible for confirming permitted use, redistribution, and attribution.
