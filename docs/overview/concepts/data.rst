Data
====

A Data...

Parameters
----------

**Required**

- ``name``, type = string

**Optional**

- ``id``, type = guid, defaults to auto-gen on creation 
- ``version``, type = string, default = ``"latest"``
- ``description``, type = string, default = ``""``
- ``tags``, type = map, default = ``{}``
- ``storage_account``, type = enum,  options: see available regions, defaults to workspace location
- ``path``, type = string, default = ``"/"``
- ``mode``, type = enum, options: ``"mount"``, ``"download"``, default = ``"mount"``

  - set to ``"download"`` to force downloading the data to each compute node

