Distributed Training
====================

You can run a distributed job by specifying the ``distribution`` section in a command job yaml file. 

The CLI currently supports the following distributed job types: MPI, TensorFlow, and PyTorch. 

MPI job
-------

Azure ML supports launching an MPI job across multiple nodes and multiple processes per node. It launches the job via ``mpirun``. If your training code uses the **Horovod** framework for distributed training, for example, you can leverage this job type to train on Azure ML.

To launch an MPI job, specify ``type: mpi`` and the number of processes per node to launch (``process_count_per_instance``) in the ``distribution`` section. If this field is not specified, Azure ML will default to launching one process per node. To run a multi-node job, specify the ``node_count`` field in the ``compute`` section.

.. literalinclude:: ../../examples/train/tensorflow/mnist-horovod/tf_horovod_job.yml
   :language: yaml
   
TensorFlow job
--------------

If you are using native distributed TensorFlow in your training code, e.g. TensorFlow 2.x's ``tf.distribute.Strategy`` API, you can run your training job on Azure ML using a TensorFlow distributed job.

To launch a distributed TensorFlow job, specify ``type: tensorflow`` and the number of workers to launch (``worker_count``) in the ``distribution`` section. To run a multi-node job, specify the ``node_count`` field in the ``compute`` section. If you are using ``tf.distribute.experimental.MultiWorkerMirroredStrategy``, your ``worker_count`` should equal the ``node_count``.

If your training code uses the parameter server strategy for distributed training, i.e. for legacy TensorFlow 1.x, you will also need to specify the number of parameter servers to use in the job via the ``parameter_server_count`` field in the ``distribution`` section.

.. literalinclude:: ../../examples/train/tensorflow/mnist-distributed/tf_distr_job.yml
   :language: yaml

In TensorFlow, the ``TF_CONFIG`` environment variable is required for training on multiple machines. Azure ML will configure and set the ``TF_CONFIG`` variable appropriately for each worker before executing your training script. You can access ``TF_CONFIG`` from your training script if you need to via ``os.environ['TF_CONFIG']``.

Example structure of TF_CONFIG set on a chief worker node:

.. code-block:: json

    TF_CONFIG='{
      "cluster": {
        "worker": ["host0:2222", "host1:2222"]
      },
      "task": {"type": "worker", "index": 0},
      "environment": "cloud"
    }'