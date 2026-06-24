# Results and Ablations

## Score progression

| Stage | Main change | Score | Absolute gain |
|---|---|---:|---:|
| Huikang SFT | Rule-induced supervised fine-tuning | 0.796 | — |
| Nemotron Math | Add mathematical reasoning replay | 0.844 | +0.048 |
| OpenMath continuation | Low-learning-rate continuation with additional long-form reasoning | **0.856** | +0.012 |

The total improvement from the first SFT stage to the best recorded score was **+0.060**.

## Interpretation

The largest gain came from adding Nemotron Math reasoning replay while keeping the same LoRA training framework. The later OpenMath continuation produced a smaller but measurable improvement. This pattern supports a progressive curriculum: first establish task-format alignment, then add broad mathematical reasoning, and finally apply a conservative continuation stage with complementary long-form examples.

## Included notebook coverage

The checked-in training notebook is the OOM-safe continued-training branch configured for a 10% Replay Math mixture. It also contains optional OpenMath handling, but OpenMath is disabled in the committed defaults to preserve the represented ablation run. The local-CV notebook is independent of the training mixture and can evaluate any compatible rank-32 adapter.

## Reproducibility caveats

Exact scores depend on the attached Kaggle data snapshots, adapter checkpoint, validation split, CUDA/runtime build, and inference parameters. The repository records the workflow and configuration but does not redistribute those external artifacts.
