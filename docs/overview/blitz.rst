Tutorial
========

Follow this 10 minute tutorial to get started with `azure.ml`.

Hello World!
------------

.. toggle::

    .. warning::
        Local execution is not in scope for private preview.

    Let's start by running our first job tracked in the cloud:

    .. code-block:: console

        az ml job create --name

    We can view it in the ML studio:

    .. tip::
        This will open your web browser! Omit the ``--web`` for the CLI view.

    .. code-block:: console 

        az ml job view --web

Hello Azure!
------------

Let's run that on the cloud!

.. code-block:: console

    az ml job create --name

Training a model
----------------

Let's train a simple lightgbm model on the Iris dataset.

.. code-block:: console

    az ml job create --name 

Tune parameters
---------------

Let's add a sweep section to the job configuration to tune the learning rate and [pick something else].

.. code-block:: console

    az ml job create --name 

Deploy to endpoint
------------------

Let's deploy the best model as an endpoint.

.. code-block:: console 

    az ml endpoint create --name

Let's test the endpoint.

.. code-block:: console 

    az ml endpoint 
    