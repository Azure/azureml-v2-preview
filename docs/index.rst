``azure.ml``
============

*Accelerate the machine learning lifecycle.*

Overview
--------

The ``azure.ml`` package provides user-friendly developer tools for Azure Machine Learning.

Goals
-----

- consistent job story
- consistent endpoint story
- all ML resources, assets, and artifacts can be serialized and exported in a human-readable format
- all jobs are composable
- reduce concepts to fundamentals

ARM Support
-----------

- improved API surface area and clean APIs for ISVs and language SDKs to be built on top of
- ARM for key uses cases (job/endpoint creation), including batch scoring endpoints
- consistent asset management experience (all assets registered via ARM, enforces consistent behavior, etc.)
- per-resource/per-asset/per-action RBAC and policy support
- x-workspace discovery, consumption, and sharing (CI/CD) of assets and resources with proper git-flow support

Timeline
--------

November 2020 (committed):
~~~~~~~~~~~~~~~~~~~~~~~~~~

- cloud execution of job (command job and sweep job)
- support for data/code/environment/model assets in jobs

March 20201 (pending):
~~~~~~~~~~~~~~~~~~~~~~

- private preview of full feature set of end-to-end training flow
- includes above plus:

  - local docker training (w/ local+data)
  - spark job support
  - workflow - full support & alignment with jobs
  - real time and batch endpoint

.. toctree::
   :hidden:
   :caption: Overview

   overview/installation.rst
   overview/setup.rst
   overview/blitz.rst
   overview/concepts.rst

.. toctree::
   :hidden:
   :caption: Quickstart 

   quickstart/jobs.rst
   quickstart/endpoints.rst

.. toctree::
   :hidden:
   :caption: Interfaces

   interfaces/cli.rst
   interfaces/python.rst

.. toctree::
   :hidden:
   :caption: Guides

   guides/local-development.rst
   guides/cloud-development.rst
   guides/distributed.rst
   guides/gha.rst
   guides/ado.rst

.. toctree::
  :hidden:
  :caption: Distributed Frameworks

  distributed/horovod.rst
  distributed/pytorch.rst
  distributed/tensorflow.rst
  distributed/spark.rst
  distributed/dask.rst
  distributed/ray.rst

.. toctree::
  :hidden:
  :caption: Reference

  reference/examples.rst
  reference/templates.rst
  reference/feedback.rst
  reference/qna.rst
  reference/troubleshooting.rst
