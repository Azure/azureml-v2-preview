Job
===

A Job...

Parameters
----------

**Required**

- ``name``, type = string
- ``command``, type = string

**Optional**

- ``id``, type = guid, defaults to auto-gen on creation 
- ``version``, type = string, default = ``"latest"``
- ``description``, type = string, default = ``""``
- ``tags``, type = map, default = ``{}``
- ``target``, type = string or azureml.Compute, default = ``"local"``
- ``environment``, type = string or azureml.Environment, default = ``""``
- ``inputs``, type = string or azureml.Data or list[string] or list[azureml.Data], default = ``""``
- ``outputs``, type = string or azureml.Data or list[string] or list[azureml.Data], default = ``""``
- ``**distributed_params``, type = params
- ``**sweep_params``, type = params

.. note:: job distribution and parameter sweeping are orthogonal

Distributed Parameters
~~~~~~~~~~~~~~~~~~~~~~

**Required**

- ``framework``, type = enum, options: ``"horovod"``, ``"pytorch"``, ``"tensorflow"``, ``"spark"``, ``"dask"``, ``"ray"``

**Optional**

See the documentation for each distributed framework for additional parameters.

Sweep Parameters
~~~~~~~~~~~~~~~~

**Required**

- ``sampling``, type = enum, options: ``"random"``, ``"bayesian"``, ``"grid"``

**Optional**

- ``termination``
- ``warm_start``
