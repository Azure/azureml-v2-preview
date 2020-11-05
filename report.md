# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az ml|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az ml` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az ml endpoint|BatchEndpoints|[commands](#CommandsInBatchEndpoints)|
|az ml datastore|Datastores|[commands](#CommandsInDatastores)|
|az ml job|Jobs|[commands](#CommandsInJobs)|
|az ml workspace|Workspaces|[commands](#CommandsInWorkspaces)|
|az ml usage|Usages|[commands](#CommandsInUsages)|
|az ml vm-size|VirtualMachineSizes|[commands](#CommandsInVirtualMachineSizes)|
|az ml compute quota|Quotas|[commands](#CommandsInQuotas)|
|az ml compute|MachineLearningCompute|[commands](#CommandsInMachineLearningCompute)|
|az ml sku|Skus|[commands](#CommandsInSkus)|

## COMMANDS
### <a name="CommandsInMachineLearningCompute">Commands in `az ml compute` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az ml compute list](#MachineLearningComputeListByWorkspace)|ListByWorkspace|[Parameters](#ParametersMachineLearningComputeListByWorkspace)|Not Found|
|[az ml compute show](#MachineLearningComputeGet)|Get|[Parameters](#ParametersMachineLearningComputeGet)|Not Found|
|[az ml compute aks create](#MachineLearningComputeCreateOrUpdate#Create#AKS)|CreateOrUpdate#Create#AKS|[Parameters](#ParametersMachineLearningComputeCreateOrUpdate#Create#AKS)|Not Found|
|[az ml compute aml-compute create](#MachineLearningComputeCreateOrUpdate#Create#AmlCompute)|CreateOrUpdate#Create#AmlCompute|[Parameters](#ParametersMachineLearningComputeCreateOrUpdate#Create#AmlCompute)|Not Found|
|[az ml compute data-factory create](#MachineLearningComputeCreateOrUpdate#Create#DataFactory)|CreateOrUpdate#Create#DataFactory|[Parameters](#ParametersMachineLearningComputeCreateOrUpdate#Create#DataFactory)|Not Found|
|[az ml compute data-lake-analytics create](#MachineLearningComputeCreateOrUpdate#Create#DataLakeAnalytics)|CreateOrUpdate#Create#DataLakeAnalytics|[Parameters](#ParametersMachineLearningComputeCreateOrUpdate#Create#DataLakeAnalytics)|Not Found|
|[az ml compute databricks create](#MachineLearningComputeCreateOrUpdate#Create#Databricks)|CreateOrUpdate#Create#Databricks|[Parameters](#ParametersMachineLearningComputeCreateOrUpdate#Create#Databricks)|Not Found|
|[az ml compute hd-insight create](#MachineLearningComputeCreateOrUpdate#Create#HDInsight)|CreateOrUpdate#Create#HDInsight|[Parameters](#ParametersMachineLearningComputeCreateOrUpdate#Create#HDInsight)|Not Found|
|[az ml compute virtual-machine create](#MachineLearningComputeCreateOrUpdate#Create#VirtualMachine)|CreateOrUpdate#Create#VirtualMachine|[Parameters](#ParametersMachineLearningComputeCreateOrUpdate#Create#VirtualMachine)|Not Found|
|[az ml compute update](#MachineLearningComputeUpdate)|Update|[Parameters](#ParametersMachineLearningComputeUpdate)|Not Found|
|[az ml compute delete](#MachineLearningComputeDelete)|Delete|[Parameters](#ParametersMachineLearningComputeDelete)|Not Found|
|[az ml compute list-key](#MachineLearningComputeListKeys)|ListKeys|[Parameters](#ParametersMachineLearningComputeListKeys)|Not Found|
|[az ml compute list-node](#MachineLearningComputeListNodes)|ListNodes|[Parameters](#ParametersMachineLearningComputeListNodes)|Not Found|

### <a name="CommandsInQuotas">Commands in `az ml compute quota` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az ml compute quota list](#QuotasList)|List|[Parameters](#ParametersQuotasList)|Not Found|
|[az ml compute quota update](#QuotasUpdate)|Update|[Parameters](#ParametersQuotasUpdate)|Not Found|

### <a name="CommandsInDatastores">Commands in `az ml datastore` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az ml datastore list](#DatastoresList)|List|[Parameters](#ParametersDatastoresList)|Not Found|
|[az ml datastore show](#DatastoresGet)|Get|[Parameters](#ParametersDatastoresGet)|Not Found|
|[az ml datastore create](#DatastoresCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersDatastoresCreateOrUpdate#Create)|Not Found|
|[az ml datastore update](#DatastoresCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersDatastoresCreateOrUpdate#Update)|Not Found|
|[az ml datastore delete](#DatastoresDelete)|Delete|[Parameters](#ParametersDatastoresDelete)|Not Found|
|[az ml datastore list-secret](#DatastoresListSecrets)|ListSecrets|[Parameters](#ParametersDatastoresListSecrets)|Not Found|

### <a name="CommandsInBatchEndpoints">Commands in `az ml endpoint` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az ml endpoint list](#BatchEndpointsList)|List|[Parameters](#ParametersBatchEndpointsList)|Not Found|
|[az ml endpoint show](#BatchEndpointsGet)|Get|[Parameters](#ParametersBatchEndpointsGet)|Not Found|
|[az ml endpoint create](#BatchEndpointsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersBatchEndpointsCreateOrUpdate#Create)|Not Found|
|[az ml endpoint update](#BatchEndpointsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersBatchEndpointsCreateOrUpdate#Update)|Not Found|
|[az ml endpoint delete](#BatchEndpointsDelete)|Delete|[Parameters](#ParametersBatchEndpointsDelete)|Not Found|
|[az ml endpoint list-key](#BatchEndpointsListKeys)|ListKeys|[Parameters](#ParametersBatchEndpointsListKeys)|Not Found|

### <a name="CommandsInJobs">Commands in `az ml job` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az ml job list](#JobsList)|List|[Parameters](#ParametersJobsList)|Not Found|
|[az ml job show](#JobsGet)|Get|[Parameters](#ParametersJobsGet)|Not Found|
|[az ml job create](#JobsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersJobsCreateOrUpdate#Create)|Not Found|
|[az ml job update](#JobsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersJobsCreateOrUpdate#Update)|Not Found|
|[az ml job delete](#JobsDelete)|Delete|[Parameters](#ParametersJobsDelete)|Not Found|
|[az ml job cancel](#JobsCancel)|Cancel|[Parameters](#ParametersJobsCancel)|Not Found|

### <a name="CommandsInSkus">Commands in `az ml sku` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az ml sku list](#SkusList)|List|[Parameters](#ParametersSkusList)|Not Found|

### <a name="CommandsInUsages">Commands in `az ml usage` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az ml usage list](#UsagesList)|List|[Parameters](#ParametersUsagesList)|Not Found|

### <a name="CommandsInVirtualMachineSizes">Commands in `az ml vm-size` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az ml vm-size list](#VirtualMachineSizesList)|List|[Parameters](#ParametersVirtualMachineSizesList)|Not Found|

### <a name="CommandsInWorkspaces">Commands in `az ml workspace` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az ml workspace list](#WorkspacesListByResourceGroup)|ListByResourceGroup|[Parameters](#ParametersWorkspacesListByResourceGroup)|Not Found|
|[az ml workspace list](#WorkspacesListBySubscription)|ListBySubscription|[Parameters](#ParametersWorkspacesListBySubscription)|Not Found|
|[az ml workspace show](#WorkspacesGet)|Get|[Parameters](#ParametersWorkspacesGet)|Not Found|
|[az ml workspace create](#WorkspacesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersWorkspacesCreateOrUpdate#Create)|Not Found|
|[az ml workspace update](#WorkspacesUpdate)|Update|[Parameters](#ParametersWorkspacesUpdate)|Not Found|
|[az ml workspace delete](#WorkspacesDelete)|Delete|[Parameters](#ParametersWorkspacesDelete)|Not Found|
|[az ml workspace list-key](#WorkspacesListKeys)|ListKeys|[Parameters](#ParametersWorkspacesListKeys)|Not Found|
|[az ml workspace resync-key](#WorkspacesResyncKeys)|ResyncKeys|[Parameters](#ParametersWorkspacesResyncKeys)|Not Found|


## COMMAND DETAILS

### group `az ml compute`
#### <a name="MachineLearningComputeListByWorkspace">Command `az ml compute list`</a>

##### <a name="ParametersMachineLearningComputeListByWorkspace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|$skiptoken|

#### <a name="MachineLearningComputeGet">Command `az ml compute show`</a>

##### <a name="ParametersMachineLearningComputeGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|

#### <a name="MachineLearningComputeCreateOrUpdate#Create#AKS">Command `az ml compute aks create`</a>

##### <a name="ParametersMachineLearningComputeCreateOrUpdate#Create#AKS">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--identity-type**|sealed-choice|The identity type.|type|type|
|**--identity-user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--ak-s-compute-location**|string|Location for the underlying compute|ak_s_compute_location|computeLocation|
|**--ak-s-description**|string|The description of the Machine Learning compute.|ak_s_description|description|
|**--ak-s-resource-id**|string|ARM resource id of the underlying compute|ak_s_resource_id|resourceId|
|**--ak-s-properties**|object|AKS properties|ak_s_properties|properties|

#### <a name="MachineLearningComputeCreateOrUpdate#Create#AmlCompute">Command `az ml compute aml-compute create`</a>

##### <a name="ParametersMachineLearningComputeCreateOrUpdate#Create#AmlCompute">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--identity-type**|sealed-choice|The identity type.|type|type|
|**--identity-user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--compute-location**|string|Location for the underlying compute|aml_compute_compute_location|computeLocation|
|**--description**|string|The description of the Machine Learning compute.|aml_compute_description|description|
|**--resource-id**|string|ARM resource id of the underlying compute|aml_compute_resource_id|resourceId|
|**--aml-compute-properties**|object|AML Compute properties|aml_compute_properties|properties|

#### <a name="MachineLearningComputeCreateOrUpdate#Create#DataFactory">Command `az ml compute data-factory create`</a>

##### <a name="ParametersMachineLearningComputeCreateOrUpdate#Create#DataFactory">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--identity-type**|sealed-choice|The identity type.|type|type|
|**--identity-user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--compute-location**|string|Location for the underlying compute|data_factory_compute_location|computeLocation|
|**--description**|string|The description of the Machine Learning compute.|data_factory_description|description|
|**--resource-id**|string|ARM resource id of the underlying compute|data_factory_resource_id|resourceId|

#### <a name="MachineLearningComputeCreateOrUpdate#Create#DataLakeAnalytics">Command `az ml compute data-lake-analytics create`</a>

##### <a name="ParametersMachineLearningComputeCreateOrUpdate#Create#DataLakeAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--identity-type**|sealed-choice|The identity type.|type|type|
|**--identity-user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--compute-location**|string|Location for the underlying compute|data_lake_analytics_compute_location|computeLocation|
|**--description**|string|The description of the Machine Learning compute.|data_lake_analytics_description|description|
|**--resource-id**|string|ARM resource id of the underlying compute|data_lake_analytics_resource_id|resourceId|
|**--data-lake-store-account-name**|string|DataLake Store Account Name|data_lake_analytics_data_lake_store_account_name|dataLakeStoreAccountName|

#### <a name="MachineLearningComputeCreateOrUpdate#Create#Databricks">Command `az ml compute databricks create`</a>

##### <a name="ParametersMachineLearningComputeCreateOrUpdate#Create#Databricks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--identity-type**|sealed-choice|The identity type.|type|type|
|**--identity-user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--compute-location**|string|Location for the underlying compute|databricks_compute_location|computeLocation|
|**--description**|string|The description of the Machine Learning compute.|databricks_description|description|
|**--resource-id**|string|ARM resource id of the underlying compute|databricks_resource_id|resourceId|
|**--databricks-access-token**|string|Databricks access token|databricks_databricks_access_token|databricksAccessToken|

#### <a name="MachineLearningComputeCreateOrUpdate#Create#HDInsight">Command `az ml compute hd-insight create`</a>

##### <a name="ParametersMachineLearningComputeCreateOrUpdate#Create#HDInsight">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--identity-type**|sealed-choice|The identity type.|type|type|
|**--identity-user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--compute-location**|string|Location for the underlying compute|hd_insight_compute_location|computeLocation|
|**--description**|string|The description of the Machine Learning compute.|hd_insight_description|description|
|**--resource-id**|string|ARM resource id of the underlying compute|hd_insight_resource_id|resourceId|
|**--ssh-port**|integer|Port open for ssh connections on the master node of the cluster.|hd_insight_ssh_port|sshPort|
|**--address**|string|Public IP address of the master node of the cluster.|hd_insight_address|address|
|**--administrator-account**|object|Admin credentials for master node of the cluster|hd_insight_administrator_account|administratorAccount|

#### <a name="MachineLearningComputeCreateOrUpdate#Create#VirtualMachine">Command `az ml compute virtual-machine create`</a>

##### <a name="ParametersMachineLearningComputeCreateOrUpdate#Create#VirtualMachine">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--identity-type**|sealed-choice|The identity type.|type|type|
|**--identity-user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--compute-location**|string|Location for the underlying compute|virtual_machine_compute_location|computeLocation|
|**--description**|string|The description of the Machine Learning compute.|virtual_machine_description|description|
|**--resource-id**|string|ARM resource id of the underlying compute|virtual_machine_resource_id|resourceId|
|**--virtual-machine-size**|string|Virtual Machine size|virtual_machine_virtual_machine_size|virtualMachineSize|
|**--ssh-port**|integer|Port open for ssh connections.|virtual_machine_ssh_port|sshPort|
|**--address**|string|Public IP address of the virtual machine.|virtual_machine_address|address|
|**--administrator-account**|object|Admin credentials for virtual machine|virtual_machine_administrator_account|administratorAccount|

#### <a name="MachineLearningComputeUpdate">Command `az ml compute update`</a>

##### <a name="ParametersMachineLearningComputeUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--scale-settings**|object|Desired scale settings for the amlCompute.|scale_settings|scaleSettings|

#### <a name="MachineLearningComputeDelete">Command `az ml compute delete`</a>

##### <a name="ParametersMachineLearningComputeDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|
|**--underlying-resource-action**|choice|Delete the underlying compute if 'Delete', or detach the underlying compute from workspace if 'Detach'.|underlying_resource_action|underlyingResourceAction|

#### <a name="MachineLearningComputeListKeys">Command `az ml compute list-key`</a>

##### <a name="ParametersMachineLearningComputeListKeys">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|

#### <a name="MachineLearningComputeListNodes">Command `az ml compute list-node`</a>

##### <a name="ParametersMachineLearningComputeListNodes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--compute-name**|string|Name of the Azure Machine Learning compute.|compute_name|computeName|

### group `az ml compute quota`
#### <a name="QuotasList">Command `az ml compute quota list`</a>

##### <a name="ParametersQuotasList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|The location for which resource usage is queried.|location|location|

#### <a name="QuotasUpdate">Command `az ml compute quota update`</a>

##### <a name="ParametersQuotasUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|The location for update quota is queried.|location|location|
|**--value**|array|The list for update quota.|value|value|

### group `az ml datastore`
#### <a name="DatastoresList">Command `az ml datastore list`</a>

##### <a name="ParametersDatastoresList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|
|**--skip-token**|string|Opaque token to retrieve the next page of results from a previous query.|skip_token|$skipToken|
|**--count**|integer|Maximum number of results to return.|count|count|
|**--is-default**|boolean|Filter down to the workspace default datastore.|is_default|isDefault|
|**--names**|array|Names of datastores to return.|names|names|
|**--search-text**|string|Text to search for in the datastore names.|search_text|searchText|
|**--order-by**|string|Order by property (createdtime | modifiedtime | name).|order_by|orderBy|
|**--order-by-asc**|boolean|Order by property in ascending order.|order_by_asc|orderByAsc|

#### <a name="DatastoresGet">Command `az ml datastore show`</a>

##### <a name="ParametersDatastoresGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Datastore name.|name|name|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|

#### <a name="DatastoresCreateOrUpdate#Create">Command `az ml datastore create`</a>

##### <a name="ParametersDatastoresCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Datastore name.|name|name|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|
|**--contents**|object||contents|contents|
|**--system-data**|object|Azure Resource Manager resource Envelope|system_data|systemData|
|**--is-default**|boolean|Whether this datastore is the default for the workspace.|is_default|isDefault|
|**--linked-info**|object||linked_info|linkedInfo|
|**--properties**|dictionary|Dictionary of :code:`<string>`|properties|properties|
|**--description**|string|The asset description text.|description|description|
|**--tags**|dictionary|Tag dictionary. Tags can be added, removed, and updated.|tags|tags|

#### <a name="DatastoresCreateOrUpdate#Update">Command `az ml datastore update`</a>

##### <a name="ParametersDatastoresCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Datastore name.|name|name|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|
|**--contents**|object||contents|contents|
|**--system-data**|object|Azure Resource Manager resource Envelope|system_data|systemData|
|**--is-default**|boolean|Whether this datastore is the default for the workspace.|is_default|isDefault|
|**--linked-info**|object||linked_info|linkedInfo|
|**--properties**|dictionary|Dictionary of :code:`<string>`|properties|properties|
|**--description**|string|The asset description text.|description|description|
|**--tags**|dictionary|Tag dictionary. Tags can be added, removed, and updated.|tags|tags|

#### <a name="DatastoresDelete">Command `az ml datastore delete`</a>

##### <a name="ParametersDatastoresDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Datastore name.|name|name|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|

#### <a name="DatastoresListSecrets">Command `az ml datastore list-secret`</a>

##### <a name="ParametersDatastoresListSecrets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Datastore name.|name|name|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|

### group `az ml endpoint`
#### <a name="BatchEndpointsList">Command `az ml endpoint list`</a>

##### <a name="ParametersBatchEndpointsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|
|**--skip-token**|string|Continuation token for pagination.|skip_token|$skipToken|

#### <a name="BatchEndpointsGet">Command `az ml endpoint show`</a>

##### <a name="ParametersBatchEndpointsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Name for the Batch Endpoint.|name|name|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|

#### <a name="BatchEndpointsCreateOrUpdate#Create">Command `az ml endpoint create`</a>

##### <a name="ParametersBatchEndpointsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Name for the Batch inference endpoint.|name|name|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|
|**--system-data**|object|Azure Resource Manager resource Envelope|system_data|systemData|
|**--description**|string|Description of the inference endpoint.|description|description|
|**--properties**|dictionary|Property dictionary. Properties can be added, but not removed or altered.|properties|properties|
|**--traffic-rules**|dictionary|Traffic rules on how the traffic will be routed across deployments.|traffic_rules|trafficRules|
|**--compute-configuration**|object|Reference to compute configuration.|compute_configuration|computeConfiguration|
|**--auth-mode**|sealed-choice|Inference endpoint authentication mode type|auth_mode|authMode|
|**--keys**|object||keys|keys|

#### <a name="BatchEndpointsCreateOrUpdate#Update">Command `az ml endpoint update`</a>

##### <a name="ParametersBatchEndpointsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Name for the Batch inference endpoint.|name|name|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|
|**--system-data**|object|Azure Resource Manager resource Envelope|system_data|systemData|
|**--description**|string|Description of the inference endpoint.|description|description|
|**--properties**|dictionary|Property dictionary. Properties can be added, but not removed or altered.|properties|properties|
|**--traffic-rules**|dictionary|Traffic rules on how the traffic will be routed across deployments.|traffic_rules|trafficRules|
|**--compute-configuration**|object|Reference to compute configuration.|compute_configuration|computeConfiguration|
|**--auth-mode**|sealed-choice|Inference endpoint authentication mode type|auth_mode|authMode|
|**--keys**|object||keys|keys|

#### <a name="BatchEndpointsDelete">Command `az ml endpoint delete`</a>

##### <a name="ParametersBatchEndpointsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Inference Endpoint name.|name|name|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|

#### <a name="BatchEndpointsListKeys">Command `az ml endpoint list-key`</a>

##### <a name="ParametersBatchEndpointsListKeys">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--name**|string|Inference Endpoint name.|name|name|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|

### group `az ml job`
#### <a name="JobsList">Command `az ml job list`</a>

##### <a name="ParametersJobsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|
|**--skip-token**|string|Continuation token for pagination.|skip_token|$skipToken|

#### <a name="JobsGet">Command `az ml job show`</a>

##### <a name="ParametersJobsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the Job.|id|id|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|

#### <a name="JobsCreateOrUpdate#Create">Command `az ml job create`</a>

##### <a name="ParametersJobsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the Job.|id|id|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|
|**--properties**|object|Additional attributes of the entity.|properties|properties|
|**--system-data**|object|Azure Resource Manager resource Envelope|system_data|systemData|

#### <a name="JobsCreateOrUpdate#Update">Command `az ml job update`</a>

##### <a name="ParametersJobsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the Job.|id|id|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|
|**--properties**|object|Additional attributes of the entity.|properties|properties|
|**--system-data**|object|Azure Resource Manager resource Envelope|system_data|systemData|

#### <a name="JobsDelete">Command `az ml job delete`</a>

##### <a name="ParametersJobsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the Job.|id|id|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|

#### <a name="JobsCancel">Command `az ml job cancel`</a>

##### <a name="ParametersJobsCancel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|The name and identifier for the Job.|id|id|
|**--subscription-id**|string||subscription_id|subscriptionId|
|**--resource-group-name**|string||resource_group_name|resourceGroupName|
|**--workspace-name**|string||workspace_name|workspaceName|

### group `az ml sku`
#### <a name="SkusList">Command `az ml sku list`</a>

##### <a name="ParametersSkusList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
### group `az ml usage`
#### <a name="UsagesList">Command `az ml usage list`</a>

##### <a name="ParametersUsagesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|The location for which resource usage is queried.|location|location|

### group `az ml vm-size`
#### <a name="VirtualMachineSizesList">Command `az ml vm-size list`</a>

##### <a name="ParametersVirtualMachineSizesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--location**|string|The location upon which virtual-machine-sizes is queried.|location|location|

### group `az ml workspace`
#### <a name="WorkspacesListByResourceGroup">Command `az ml workspace list`</a>

##### <a name="ParametersWorkspacesListByResourceGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--skiptoken**|string|Continuation token for pagination.|skiptoken|$skiptoken|

#### <a name="WorkspacesListBySubscription">Command `az ml workspace list`</a>

##### <a name="ParametersWorkspacesListBySubscription">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="WorkspacesGet">Command `az ml workspace show`</a>

##### <a name="ParametersWorkspacesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="WorkspacesCreateOrUpdate#Create">Command `az ml workspace create`</a>

##### <a name="ParametersWorkspacesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--location**|string|Specifies the location of the resource.|location|location|
|**--tags**|dictionary|Contains resource tags defined as key/value pairs.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--identity-type**|sealed-choice|The identity type.|type|type|
|**--identity-user-assigned-identities**|dictionary|The user assigned identities associated with the resource.|user_assigned_identities|userAssignedIdentities|
|**--description**|string|The description of this workspace.|description|description|
|**--friendly-name**|string|The friendly name for this workspace. This name in mutable|friendly_name|friendlyName|
|**--key-vault**|string|ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created|key_vault|keyVault|
|**--application-insights**|string|ARM id of the application insights associated with this workspace. This cannot be changed once the workspace has been created|application_insights|applicationInsights|
|**--container-registry**|string|ARM id of the container registry associated with this workspace. This cannot be changed once the workspace has been created|container_registry|containerRegistry|
|**--storage-account**|string|ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created|storage_account|storageAccount|
|**--discovery-url**|string|Url for the discovery service to identify regional endpoints for machine learning experimentation services|discovery_url|discoveryUrl|
|**--hbi-workspace**|boolean|The flag to signal HBI data in the workspace and reduce diagnostic data collected by the service|hbi_workspace|hbiWorkspace|
|**--image-build-compute**|string|The compute name for image build|image_build_compute|imageBuildCompute|
|**--allow-public-access-when-behind-vnet**|boolean|The flag to indicate whether to allow public access when behind VNet.|allow_public_access_when_behind_vnet|allowPublicAccessWhenBehindVnet|
|**--shared-private-link-resources**|array|The list of shared private link resources in this workspace.|shared_private_link_resources|sharedPrivateLinkResources|
|**--encryption-status**|choice|Indicates whether or not the encryption is enabled for the workspace.|status|status|
|**--encryption-key-vault-properties**|object|Customer Key vault properties.|key_vault_properties|keyVaultProperties|

#### <a name="WorkspacesUpdate">Command `az ml workspace update`</a>

##### <a name="ParametersWorkspacesUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
|**--tags**|dictionary|The resource tags for the machine learning workspace.|tags|tags|
|**--sku**|object|The sku of the workspace.|sku|sku|
|**--description**|string|The description of this workspace.|description|description|
|**--friendly-name**|string|The friendly name for this workspace.|friendly_name|friendlyName|

#### <a name="WorkspacesDelete">Command `az ml workspace delete`</a>

##### <a name="ParametersWorkspacesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="WorkspacesListKeys">Command `az ml workspace list-key`</a>

##### <a name="ParametersWorkspacesListKeys">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|

#### <a name="WorkspacesResyncKeys">Command `az ml workspace resync-key`</a>

##### <a name="ParametersWorkspacesResyncKeys">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|Name of the resource group in which workspace is located.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|Name of Azure Machine Learning workspace.|workspace_name|workspaceName|
