Compute Resources
=======

A compute target is a designated compute resource or environment where you run your jobs and endpoints run.
Using compute targets makes it easy for you to later change your compute environment without having to change your code.

In a typical model development lifecycle, you might:

1. Start by developing and experimenting on a small amount of data. At this stage, use your local environment, such as a local computer or cloud-based virtual machine (VM), as your compute target.
2. Scale up to larger data, or do distributed training by using one of these training compute targets.
3. After your model is ready, deploy it to a web hosting environment or IoT device with one of these deployment compute targets.

The compute resources you use for your compute targets are attached to a workspace. Compute resources other than the local machine are shared by users of the workspace.


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

