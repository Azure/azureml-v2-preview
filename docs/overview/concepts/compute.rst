Compute
=======

A Compute...

Parameters
----------

**Required**

- ``name``, type = string

**Optional**

- ``id``, type = guid, defaults to auto-gen on creation 
- ``description``, type = string, default = ``""``
- ``tags``, type = map, default = ``{}``
- ``location``, type = enum,  options: see available regions, defaults to workspace location
- ``vm_size``, type = enum, options: see available options, defaults = ``"Standard_DS3_v2"``
- ``virtual_network``, type = string, defaults to workspace virtual network
- ``min_nodes``, type = int, default = ``0``
- ``max_nodes``, type = int, default = ``1``
- ``idle_timeout``, type = int, default = ``30``

  - idle timeout for node de-allocation in seconds

