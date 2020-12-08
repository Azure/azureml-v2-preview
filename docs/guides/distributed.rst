Distributed Processing
======================

Distributed processing is easy with `azureml`.

Overview
--------

Generally, you should only consider distributed processing when it is necessary. For example, you might first consider:

- using a subset of data
- using a larger vm
- clever optimizations

However, it is common to need distributed processing for large-scale machine learning.

EDA & Visualization
-------------------

**Recommended**

- dataframes via Spark or Dask
- SQL via Spark or Dask
- xarray via Dask

Data Engineering
----------------

**Recommended**

- Spark
- Dask

Classical ML
------------

**Recommended**

- scikit-learn via Dask or Ray
- MLLib via Spark
- dask-ml via Dask

Gradient Boosting Machine (GBM)
-------------------------------

**Recommended**

- LightGBM via Dask or Spark
- XGBoost via Dask

Hyperparameter Tuning
---------------------

**Recommended**

- Tune via Ray
- Optuna via Dask

Deep Learning
-------------

**Recommended**

- PyTorch via Horovod or PyTorch

  - fastai
  - PyTorch-Lightning
  - DeepSpeed

- Tensorflow via Horovod or Tensorflow

  - keras


Reinforcement Learning
----------------------

**Recommended**

- VopalWabbit via Spark
- RLlib via Ray

Hardware Acceleration
---------------------

Each distribution framework supports hardware acceleration on Graphical Processing Units (GPUs) which are available through Azure. See the corresponding framework for details.
