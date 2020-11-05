---
title: README
slug: /userguide/
---

Welcome to the AML User Guide!

## Prerequisites

1. An Azure subscription. If you don't have an Azure subscription, [create a free account](https://aka.ms/amlfree) before you begin.
2. A terminal.

## Install the CLI

We have pre-built the Azure ML CLI as part of this Git repository. Simply run the following commands to set up your CLI environment:

> MacOS? `brew install wget`

```console
wget https://mldevplatv2.blob.core.windows.net/cli/cli.zip
tar xvf cli.zip -C .
set AZURE_EXTENSION_DIR=./azext_ml
az ml -h
```

This should show off the new set of AZ CLI commands and you'll be all set to get started.

## Creating a job

Prepare the code you'd like to run. For this example, we'll simply clone LightGBM from GitHub and run an example:

```console
git clone https://github.com/Microosft/lightgbm
```

CLI example: ```az ml job create jobspec.yaml```

**Command Job:**

```yaml
name: lightgbm
run:
  code: ./lightgbm/examples
  command: python ./python-guide/advanced_example.py --lr 0.01 --feature_fraction 0.7 --bagging_fraction 0.6
  environment:
    name: lightgbm
compute: goazurego
```

**Sweep Job:**

```yaml
name: lightgbm-sweep
algorithm: random
search_space:
  lr:
    spec: uniform
    min_value: 0.01
    max_value: 0.1
objective:
  primary_metric: rmse
  goal: minimize
trial:
  code: ./lightgbm/examples
  command: python ./python-guide/advanced_example.py  --lr {search_space.lr} --feature_fraction 0.7 --bagging_fraction 0.6
  environment: lightgbm
early_termination:
  spec: median
  evaluation_interval: 1
  delay_evaluation: 5
compute: goazurego
```
