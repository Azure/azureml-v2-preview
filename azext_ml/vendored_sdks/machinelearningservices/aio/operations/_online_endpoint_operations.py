# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class OnlineEndpointOperations:
    """OnlineEndpointOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure_machine_learning_workspaces.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        api_version: Optional[str] = "1.0.0",
        **kwargs
    ) -> AsyncIterable["models.OnlineEndpointPropertiesTrackedResourceArmPaginatedResult"]:
        """List Online Endpoints.

        List Online Endpoints.

        :param subscription_id:
        :type subscription_id: str
        :param resource_group_name:
        :type resource_group_name: str
        :param workspace_name:
        :type workspace_name: str
        :param api_version: Api Version.
        :type api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either OnlineEndpointPropertiesTrackedResourceArmPaginatedResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure_machine_learning_workspaces.models.OnlineEndpointPropertiesTrackedResourceArmPaginatedResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.OnlineEndpointPropertiesTrackedResourceArmPaginatedResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if api_version is not None:
                    query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('OnlineEndpointPropertiesTrackedResourceArmPaginatedResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/onlineEndpoints'}  # type: ignore

    async def delete(
        self,
        name: str,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        api_version: Optional[str] = "1.0.0",
        **kwargs
    ) -> None:
        """Delete Online Endpoint.

        Delete Online Endpoint.

        :param name: Online Endpoint name.
        :type name: str
        :param subscription_id:
        :type subscription_id: str
        :param resource_group_name:
        :type resource_group_name: str
        :param workspace_name:
        :type workspace_name: str
        :param api_version: Api Version.
        :type api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if api_version is not None:
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/onlineEndpoints/{name}'}  # type: ignore

    async def get(
        self,
        name: str,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        api_version: Optional[str] = "1.0.0",
        **kwargs
    ) -> "models.OnlineEndpointPropertiesTrackedResource":
        """Get Online Endpoint.

        Get Online Endpoint.

        :param name: Online Endpoint name.
        :type name: str
        :param subscription_id:
        :type subscription_id: str
        :param resource_group_name:
        :type resource_group_name: str
        :param workspace_name:
        :type workspace_name: str
        :param api_version: Api Version.
        :type api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: OnlineEndpointPropertiesTrackedResource, or the result of cls(response)
        :rtype: ~azure_machine_learning_workspaces.models.OnlineEndpointPropertiesTrackedResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.OnlineEndpointPropertiesTrackedResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if api_version is not None:
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('OnlineEndpointPropertiesTrackedResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/onlineEndpoints/{name}'}  # type: ignore

    async def create_or_update(
        self,
        name: str,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        api_version: Optional[str] = "1.0.0",
        body: Optional["models.OnlineEndpointPropertiesTrackedResource"] = None,
        **kwargs
    ) -> "models.OnlineEndpointPropertiesTrackedResource":
        """Create or update Online Endpoint.

        Create or update Online Endpoint.

        :param name: Online Endpoint name.
        :type name: str
        :param subscription_id:
        :type subscription_id: str
        :param resource_group_name:
        :type resource_group_name: str
        :param workspace_name:
        :type workspace_name: str
        :param api_version: Api Version.
        :type api_version: str
        :param body: Online Endpoint entity to apply during operation.
        :type body: ~azure_machine_learning_workspaces.models.OnlineEndpointPropertiesTrackedResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: OnlineEndpointPropertiesTrackedResource, or the result of cls(response)
        :rtype: ~azure_machine_learning_workspaces.models.OnlineEndpointPropertiesTrackedResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.OnlineEndpointPropertiesTrackedResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if api_version is not None:
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if body is not None:
            body_content = self._serialize.body(body, 'OnlineEndpointPropertiesTrackedResource')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('OnlineEndpointPropertiesTrackedResource', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('OnlineEndpointPropertiesTrackedResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/onlineEndpoints/{name}'}  # type: ignore

    async def regenerate_key(
        self,
        name: str,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        api_version: Optional[str] = "1.0.0",
        key_type: Optional[Union[str, "models.KeyType"]] = None,
        key_value: Optional[str] = None,
        **kwargs
    ) -> None:
        """Regenerate AuthKeys for an Endpoint using Key-based authentication.

        Regenerate AuthKeys for an Endpoint using Key-based authentication.

        :param name: Online Endpoint name.
        :type name: str
        :param subscription_id:
        :type subscription_id: str
        :param resource_group_name:
        :type resource_group_name: str
        :param workspace_name:
        :type workspace_name: str
        :param api_version: Api Version.
        :type api_version: str
        :param key_type: Specification for which type of key to generate. Primary or Secondary.
        :type key_type: str or ~azure_machine_learning_workspaces.models.KeyType
        :param key_value: The value the key is set to.
        :type key_value: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        body = models.RegenerateEndpointKeysRequest(key_type=key_type, key_value=key_value)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.regenerate_key.metadata['url']  # type: ignore
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if api_version is not None:
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if body is not None:
            body_content = self._serialize.body(body, 'RegenerateEndpointKeysRequest')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    regenerate_key.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/onlineEndpoints/{name}/regenerateKeys'}  # type: ignore

    async def list_key(
        self,
        name: str,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        api_version: Optional[str] = "1.0.0",
        **kwargs
    ) -> "models.AuthKeys":
        """List AuthKeys for an Endpoint using Key-based authentication.

        List AuthKeys for an Endpoint using Key-based authentication.

        :param name: Online Endpoint name.
        :type name: str
        :param subscription_id:
        :type subscription_id: str
        :param resource_group_name:
        :type resource_group_name: str
        :param workspace_name:
        :type workspace_name: str
        :param api_version: Api Version.
        :type api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AuthKeys, or the result of cls(response)
        :rtype: ~azure_machine_learning_workspaces.models.AuthKeys
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AuthKeys"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.list_key.metadata['url']  # type: ignore
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if api_version is not None:
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AuthKeys', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list_key.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/onlineEndpoints/{name}/listKeys'}  # type: ignore

    async def get_token(
        self,
        name: str,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        api_version: Optional[str] = "1.0.0",
        **kwargs
    ) -> "models.AuthToken":
        """Retrieve a valid AAD token for an Endpoint using AMLToken-based authentication.

        Retrieve a valid AAD token for an Endpoint using AMLToken-based authentication.

        :param name: Online Endpoint name.
        :type name: str
        :param subscription_id:
        :type subscription_id: str
        :param resource_group_name:
        :type resource_group_name: str
        :param workspace_name:
        :type workspace_name: str
        :param api_version: Api Version.
        :type api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AuthToken, or the result of cls(response)
        :rtype: ~azure_machine_learning_workspaces.models.AuthToken
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AuthToken"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_token.metadata['url']  # type: ignore
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if api_version is not None:
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AuthToken', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_token.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/onlineEndpoints/{name}/token'}  # type: ignore
