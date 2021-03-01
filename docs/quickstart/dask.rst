Running a DASK job
==================

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
  Due to a bug, your cluster nodes need to have enough free space on the `/tmp` volume to accomodate the whole dataset used, 
  which will be 24GB in the case of `--months 12`. Using STANDARD_D15_V2 VMs to build your cluster will give you close to 1TB of
  free disk space and works well even for bigger datasets.

For debugging and interactive work, the script also launches a Jupyter server on the first node which can be accessed most 
easily from a Compute Instance deployed to the same VNet as the Compute Cluster. 

If a --script parameter is provided, then the script will run that script after the cluster has been brought up and the job 
will be terminated after the script has completed. To start a DASK cluster for interactive work, don't provide a --script parameter, 
which will have the job run indefinitely (i.e. until you terminate it).

The job below is currently launched as a pytorch job since that gives the full flexibility of assigning the work to the 
different nodes of the cluster by just checking the $RANK environment variable. In the future we will provide a more generic 
name for that mode of launching a distributed job.

.. literalinclude:: ../../examples/dask/dask-job.yaml
   :language: yaml