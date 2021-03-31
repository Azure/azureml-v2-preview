Deploy Models (WIP)
===================

.. warning::
    This documentation is not fully functional. Endpoint creation is officially launching in January.

Models can be deployed as online or batch mode Endpoints.

An Endpoint is an instantiation of your model into either a web service that can be hosted in the cloud or an IoT module for integrated device deployments.
Below are two examples creating an endpoint.



.. literalinclude:: ../../examples/deploy/sklearn/basicaksendpoint.yml
   :language: yaml

To create the endpoint, run the following:

.. code-block:: console

  az ml endpoint create --file basicaksendpoint.yml

Minimal endpoint specification - batch
--------------------------------------

.. code-block:: yaml

  name: myBatchEndpoint
  type: batch
  auth_mode: AMLToken
  deployments:
    blue:    
      model: azureml:models/sklearn_regression_model:1
      code_configuration:
        code:
          directory: ./endpoint
        scoring_script: ./test.py
      environment: azureml:AzureML-Minimal/versions/1
      scale_settings: 
        node_count: 1
      mini_batch_size: 5  
      output_configuration:
        output_action: AppendRow 
        append_row_file_name: append_row.txt
      retry_settings:
        max_retries: 3
        timeout: 30  
      error_threshold: 10
      logging_level: info  
      compute:
        target: azureml:cpu-cluster

.. code-block:: console

  az ml endpoint create --file batchendpoint.yml
  `  