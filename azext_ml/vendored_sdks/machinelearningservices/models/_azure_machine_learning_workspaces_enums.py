# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AcquisitionFunction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Aquisition function
    """

    EI = "EI"
    PI = "PI"
    UCB = "UCB"

class AllocationState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Allocation state of the compute. Possible values are: steady - Indicates that the compute is
    not resizing. There are no changes to the number of compute nodes in the compute in progress. A
    compute enters this state when it is created and when no operations are being performed on the
    compute to change the number of compute nodes. resizing - Indicates that the compute is
    resizing; that is, compute nodes are being added to or removed from the compute.
    """

    STEADY = "Steady"
    RESIZING = "Resizing"

class BatchLoggingLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Logging level for batch inference operation.
    """

    INFO = "Info"
    WARNING = "Warning"
    DEBUG = "Debug"

class BatchOutputAction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates how the output will be organized.
    """

    SUMMARY_ONLY = "SummaryOnly"
    APPEND_ROW = "AppendRow"

class BillingCurrency(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Three lettered code specifying the currency of the VM price. Example: USD
    """

    USD = "USD"

class CommunicationBackend(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NCCL = "Nccl"
    GLOO = "Gloo"

class ComputeEnvironmentType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The compute environment type for the service.
    """

    ACI = "ACI"
    AKS = "AKS"

class ComputeType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    AML_COMPUTE = "AMLCompute"
    AKS = "AKS"
    ACI = "ACI"
    DATA_FACTORY = "DataFactory"
    VIRTUAL_MACHINE = "VirtualMachine"
    HD_INSIGHT = "HDInsight"
    DATABRICKS = "Databricks"
    DATA_LAKE_ANALYTICS = "DataLakeAnalytics"

class ContentsType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Storage type backing the datastore.
    """

    AZURE_BLOB = "AzureBlob"
    AZURE_DATA_LAKE = "AzureDataLake"
    AZURE_DATA_LAKE_GEN2 = "AzureDataLakeGen2"
    AZURE_FILE = "AzureFile"
    AZURE_MY_SQL = "AzureMySql"
    AZURE_POSTGRE_SQL = "AzurePostgreSql"
    AZURE_SQL_DATABASE = "AzureSqlDatabase"
    GLUSTER_FS = "GlusterFs"

class CredentialsType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Credential type used to authentication with storage.
    """

    ACCOUNT_KEY = "AccountKey"
    CERTIFICATE = "Certificate"
    SAS = "Sas"
    SERVICE_PRINCIPAL = "ServicePrincipal"
    SQL_ADMIN = "SqlAdmin"

class CustomAssetType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Custom asset type
    RL currently use this type to store explanations and faireness data
    """

    AZUREML_EXPLANATION = "AzuremlExplanation"
    AZUREML_FAIRNESS = "AzuremlFairness"
    AZUREML_MODEL = "AzuremlModel"

class DataBindingMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Mechanism for accessing the data artifact.
    """

    MOUNT = "Mount"
    DOWNLOAD = "Download"
    UPLOAD = "Upload"

class DatasetConsumptionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    RUN_INPUT = "RunInput"
    REFERENCE = "Reference"

class DatasetDeliveryMechanism(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DIRECT = "Direct"
    MOUNT = "Mount"
    DOWNLOAD = "Download"

class DatasetOutputMechanism(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UPLOAD = "Upload"
    MOUNT = "Mount"

class DatasetOutputType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    RUN_OUTPUT = "RunOutput"
    REFERENCE = "Reference"

class DatasetType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The Format of dataset.
    """

    SIMPLE = "Simple"
    DATAFLOW = "Dataflow"

class DeploymentProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state for the endpoint deployment.
    """

    CREATING = "Creating"
    DELETING = "Deleting"
    SCALING = "Scaling"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"

class DeploymentType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The deployment type for the service.
    """

    GRPC_REALTIME_ENDPOINT = "GRPCRealtimeEndpoint"
    HTTP_REALTIME_ENDPOINT = "HttpRealtimeEndpoint"
    BATCH = "Batch"

class DistributionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the type of distibution framework.
    """

    PY_TORCH = "PyTorch"
    TENSORFLOW = "Tensorflow"
    MPI = "Mpi"

class DockerSpecificationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of Docker Properties specified
    """

    DOCKERFILE = "Dockerfile"
    DOCKER_IMAGE = "DockerImage"

class EarlyTerminationPolicyType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Name of policy configuration
    """

    BANDIT = "Bandit"
    MEDIAN_STOPPING = "MedianStopping"
    TRUNCATION_SELECTION = "TruncationSelection"

class EncryptionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates whether or not the encryption is enabled for the workspace.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class EndpointAuthModeType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Inference endpoint authentication mode type
    """

    AML_TOKEN = "AMLToken"
    KEY = "Key"

class EndpointProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """State of provisioning
    """

    CREATING = "Creating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"

class Enum0(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "Default"
    ALL = "All"
    ACTIVE_ONLY = "ActiveOnly"
    ARCHIVED_ONLY = "ArchivedOnly"

class Enum2(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASC = "Asc"
    DESC = "Desc"

class Enum3(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "Default"
    NONE = "None"
    MERGE_TO_VECTOR = "MergeToVector"

class Enum4(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "None"
    REPORT_UNMERGED_METRICS_VALUES = "ReportUnmergedMetricsValues"

class Enum5(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SELECT_ALL = "SelectAll"
    SELECT_BY_FIRST_VALUE_SCHEMA = "SelectByFirstValueSchema"

class EnvironmentSpecificationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Environment specification is either user managed or curated by the Azure ML service
    
    
    .. raw:: html
    
       <see href="https://docs.microsoft.com/en-us/azure/machine-learning/resource-curated-
    environments" />
    """

    CURATED = "Curated"
    USER_CREATED = "UserCreated"

class ExperimentQueryParamsDtoViewType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "Default"
    ALL = "All"
    ACTIVE_ONLY = "ActiveOnly"
    ARCHIVED_ONLY = "ArchivedOnly"

class ExportFormatType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The format of exported labels.
    """

    DATASET = "Dataset"
    COCO = "Coco"
    CSV = "CSV"

class FlowType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    MOVEMENT = "Movement"
    MATERIALIZE = "Materialize"
    TRANSFORMATION = "Transformation"

class ImageAnnotationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Annotation type of image labeling job.
    """

    CLASSIFICATION = "Classification"
    BOUNDING_BOX = "BoundingBox"
    INSTANCE_SEGMENTATION = "InstanceSegmentation"

class JobStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the job.
    """

    NOT_STARTED = "NotStarted"
    STARTING = "Starting"
    PROVISIONING = "Provisioning"
    PREPARING = "Preparing"
    QUEUED = "Queued"
    RUNNING = "Running"
    FINALIZING = "Finalizing"
    CANCEL_REQUESTED = "CancelRequested"
    COMPLETED = "Completed"
    FAILED = "Failed"
    CANCELED = "Canceled"
    NOT_RESPONDING = "NotResponding"
    PAUSED = "Paused"

class JobType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the type of job.
    """

    COMMAND = "Command"
    SWEEP = "Sweep"
    LABELING = "Labeling"
    PIPELINE = "Pipeline"
    DATA = "Data"
    AUTO_ML = "AutoML"

class KeyType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specification for which type of key to generate. Primary or Secondary.
    """

    PRIMARY = "Primary"
    SECONDARY = "Secondary"

class LabelExportState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The state of the Export Labels operation.
    """

    REQUESTED = "Requested"
    RUNNING = "Running"
    FAILED = "Failed"
    COMPLETED = "Completed"

class MediaType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Media type of the job.
    """

    IMAGE = "Image"
    TEXT = "Text"

class NodeState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """State of the compute node. Values are idle, running, preparing, unusable, leaving and
    preempted.
    """

    IDLE = "idle"
    RUNNING = "running"
    PREPARING = "preparing"
    UNUSABLE = "unusable"
    LEAVING = "leaving"
    PREEMPTED = "preempted"

class OptimizationMetric(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    AUC_WEIGHTED = "AUC_weighted"
    ACCURACY = "Accuracy"
    NORM_MACRO_RECALL = "Norm_macro_recall"
    AVERAGE_PRECISION_SCORE_WEIGHTED = "Average_precision_score_weighted"
    PRECISION_SCORE_WEIGHTED = "Precision_score_weighted"
    SPEARMAN_CORRELATION = "Spearman_correlation"
    NORMALIZED_ROOT_MEAN_SQUARED_ERROR = "Normalized_root_mean_squared_error"
    R2_SCORE = "R2_score"
    NORMALIZED_MEAN_ABSOLUTE_ERROR = "Normalized_mean_absolute_error"
    NORMALIZED_ROOT_MEAN_SQUARED_LOG_ERROR = "Normalized_root_mean_squared_log_error"
    MEAN_AVERAGE_PRECISION = "Mean_average_precision"
    IOU = "Iou"

class OrderString(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    CREATED_AT_DESC = "CreatedAtDesc"
    CREATED_AT_ASC = "CreatedAtAsc"
    UPDATED_AT_DESC = "UpdatedAtDesc"
    UPDATED_AT_ASC = "UpdatedAtAsc"

class OsType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Compute OS Type
    """

    LINUX = "Linux"
    WINDOWS = "Windows"

class ParameterSamplingType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the hyperparameter sampling algorithms
    """

    GRID = "Grid"
    RANDOM = "Random"
    BAYESIAN = "Bayesian"

class PrimaryMetricGoal(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Defines supported metric goals for hyperparameter tuning
    """

    MINIMIZE = "Minimize"
    MAXIMIZE = "Maximize"

class PrivateEndpointConnectionProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current provisioning state.
    """

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"

class PrivateEndpointServiceConnectionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The private endpoint connection status.
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"
    TIMEOUT = "Timeout"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current deployment state of workspace resource. The provisioningState is to indicate states
    for resource provisioning.
    """

    UNKNOWN = "Unknown"
    UPDATING = "Updating"
    CREATING = "Creating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"

class PythonSpecificationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Python specification type must be either Pip Requirements or a Conda Environment File
    """

    CONDA_ENVIRONMENT = "CondaEnvironment"
    PIP_REQUIREMENTS = "PipRequirements"

class QuotaUnit(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """An enum describing the unit of quota measurement.
    """

    COUNT = "Count"

class ReasonCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The reason for the restriction.
    """

    NOT_SPECIFIED = "NotSpecified"
    NOT_AVAILABLE_FOR_REGION = "NotAvailableForRegion"
    NOT_AVAILABLE_FOR_SUBSCRIPTION = "NotAvailableForSubscription"

class ReferenceType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the type of asset reference.
    """

    ID = "Id"
    DATA_PATH = "DataPath"
    OUTPUT_PATH = "OutputPath"

class RemoteLoginPortPublicAccess(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """State of the public SSH port. Possible values are: Disabled - Indicates that the public ssh
    port is closed on all nodes of the cluster. Enabled - Indicates that the public ssh port is
    open on all nodes of the cluster. NotSpecified - Indicates that the public ssh port is closed
    on all nodes of the cluster if VNet is defined, else is open all public nodes. It can be
    default only during cluster creation time, after creation it will be either enabled or
    disabled.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"
    NOT_SPECIFIED = "NotSpecified"

class ResourceIdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The identity type.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"
    USER_ASSIGNED = "UserAssigned"
    NONE = "None"

class ScaleTypeMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    AUTOMATIC = "Automatic"
    MANUAL = "Manual"
    NONE = "None"

class SSLConfigurationStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enable or disable ssl for scoring
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"

class Status(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of update workspace quota.
    """

    UNDEFINED = "Undefined"
    SUCCESS = "Success"
    FAILURE = "Failure"
    INVALID_QUOTA_BELOW_CLUSTER_MINIMUM = "InvalidQuotaBelowClusterMinimum"
    INVALID_QUOTA_EXCEEDS_SUBSCRIPTION_LIMIT = "InvalidQuotaExceedsSubscriptionLimit"
    INVALID_VM_FAMILY_NAME = "InvalidVMFamilyName"
    OPERATION_NOT_SUPPORTED_FOR_SKU = "OperationNotSupportedForSku"
    OPERATION_NOT_ENABLED_FOR_REGION = "OperationNotEnabledForRegion"

class StatusMessageLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Severity level of message.
    """

    ERROR = "Error"
    INFORMATION = "Information"
    WARNING = "Warning"

class TrainingType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Training type
    """

    TRAIN_FULL = "TrainFull"
    TRAIN_AND_VALIDATE = "TrainAndValidate"
    CROSS_VALIDATE = "CrossValidate"
    MEAN_CROSS_VALIDATE = "MeanCrossValidate"

class UnderlyingResourceAction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DELETE = "Delete"
    DETACH = "Detach"

class UnitOfMeasure(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The unit of time measurement for the specified VM price. Example: OneHour
    """

    ONE_HOUR = "OneHour"

class UsageUnit(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """An enum describing the unit of usage measurement.
    """

    COUNT = "Count"

class UserType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """the type of identity that created the resource: user, application, managedIdentity, key
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class VariantType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the variant.
    """

    CONTROL = "Control"
    TREATMENT = "Treatment"

class VmPriceOsType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Operating system type used by the VM.
    """

    LINUX = "Linux"
    WINDOWS = "Windows"

class VmPriority(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Virtual Machine priority
    """

    DEDICATED = "Dedicated"
    LOW_PRIORITY = "LowPriority"

class VmTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the VM.
    """

    STANDARD = "Standard"
    LOW_PRIORITY = "LowPriority"
    SPOT = "Spot"

class WebServiceState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current state of the service.
    """

    TRANSITIONING = "Transitioning"
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    FAILED = "Failed"
    UNSCHEDULABLE = "Unschedulable"
