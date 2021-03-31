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

Running a DASK job
------------------

Please see `here for the full example code <https://github.com/Azure/azureml-v2-preview/tree/main/examples/dask>`_ .

This example shows how a distribted DASK job can be run on multiple nodes of a cluster. In this example we are using 4 nodes 
using this job yaml. The startup of the cluster is done by the `startDask.py` script which launches a scheduler
and a worker on the first node of the cluster and a worker on all the other nodes.

.. note::
  Before running the sample, the data needs to be copied to the datastore using the script `python copy_nyc_taxi.py --months 1` 
  (`--months` being the number of months data to upload). This will upload the data to a dataset `nyctaxi` on the workspace. 
  Note that, depending on the number of months, the script copies up to 24 GB of data (down and then up to the workspace), so 
  it is strongly recommended to do this with good connectivity. It works well when run on from an AzureML compute instance 
  (takes about 20 minutes). 

.. note::
  Since the script is writing the output to the local drive, and since the dataset is cached on the same local drive,
  your cluster nodes need to have enough free space on the local volume to accomodate pretty much the whole input and output datasets used (to be on the safe side). 
  The input dataset will be 24GB in the case of `--months 12`, the parquet output is about 4GB. Using STANDARD_D15_V2 VMs to build your cluster will give you close to 1TB of
  free disk space and works well even for bigger datasets.

If a --script parameter is provided, then the script will run that script after the cluster has been brought up and the job 
will be terminated after the script has completed. To start a DASK cluster for interactive work, don't provide a --script parameter, 
which will have the job run indefinitely (i.e. until you terminate it).

The job below is currently launched as a pytorch job since that gives the full flexibility of assigning the work to the 
different nodes of the cluster by just checking the $RANK environment variable. In the future we will provide a more generic 
name for that mode of launching a distributed job.

.. literalinclude:: ../../examples/dask/dask-job.yaml
  :language: yaml

For debugging and interactive work, the script also launches a Jupyter server on the first node which can be accessed by ssh tunnelling into
a node of the cluster (assuming the cluster is not in a VNet). Make sure to provide your SSH public key while setting up the cluster (in ml.azure.com Create Compute Cluster/Settings/Enable SSH access/Use existing public key).
Then, on your local laptop computer, you can run a command similar to the one below:

.. code-block:: console

  ssh azureuser@20.67.29.11 -p 50000 -L 9999:10.0.0.4:8888 -L 9797:10.0.0.4:8787

In the above example:

- ``20.67.29.11`` is the public IP address of any of the nodes on the cluster (find in ml.azure.com under Compute/Compute Clusters/<cluster name>/Nodes)
- ``50000`` is the port of that same node
- ``9999`` and ``9797`` are the ports where the jupyter server and the dask dashboard will be reachable on your local machine
- ``10.0.0.4`` is the private IP of the head node of the job, as will be logged by the job and show up in run history (find in ml.azure.com under Experiments/dask/<run id>/details/metrics/headnode) 

Then you should be able to access the following urls:

- ``http://localhost:9999?token=<jupyter-token>`` for Jupyter, where <jupyter-token> is jupyter-token that will show up in run history (find in ml.azure.com under Experiments/dask/<run id>/details/metrics/jupyter-token) 
- ``http://localhost:9797`` for the Dask Dashboard
