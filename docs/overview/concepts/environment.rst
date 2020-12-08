Environment
===========

An Environment...

Parameters
----------

**Required**

- ``name``, type = string

**Optional**

- ``id``, type = guid, defaults to auto-gen on creation 
- ``version``, type = string, default = ``"latest"``
- ``description``, type = string, default = ``""``
- ``tags``, type = map, default = ``{}``
- ``docker_image``, type = string, default = ``"azureml/default"``
- ``docker_file``, type = string, default = ``""``
- ``conda_file``, type = string, default = ``""``
- ``pip_file``, type = string, default = ``""``
