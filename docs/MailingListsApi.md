# Moosend.Wrappers.PythonWrapper.MailingListsApi

All URIs are relative to *https://api.moosend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**creating_a_custom_field**](MailingListsApi.md#creating_a_custom_field) | **POST** /lists/{MailingListID}/customfields/create.{Format} | Creating a custom field
[**creating_a_mailing_list**](MailingListsApi.md#creating_a_mailing_list) | **POST** /lists/create.{Format} | Creating a mailing list
[**deleting_a_mailing_list**](MailingListsApi.md#deleting_a_mailing_list) | **DELETE** /lists/{MailingListID}/delete.{Format} | Deleting a mailing list
[**getting_all_active_mailing_lists**](MailingListsApi.md#getting_all_active_mailing_lists) | **GET** /lists.{Format} | Getting all active mailing lists
[**getting_all_active_mailing_lists_with_paging**](MailingListsApi.md#getting_all_active_mailing_lists_with_paging) | **GET** /lists/{Page}/{PageSize}.{Format} | Getting all active mailing lists with paging
[**getting_mailing_list_details**](MailingListsApi.md#getting_mailing_list_details) | **GET** /lists/{MailingListID}/details.{Format} | Getting mailing list details
[**removing_a_custom_field**](MailingListsApi.md#removing_a_custom_field) | **DELETE** /lists/{MailingListID}/customfields/{CustomFieldID}/delete.{Format} | Removing a custom field
[**updating_a_custom_field**](MailingListsApi.md#updating_a_custom_field) | **POST** /lists/{MailingListID}/customfields/{CustomFieldID}/update.{Format} | Updating a custom field
[**updating_a_mailing_list**](MailingListsApi.md#updating_a_mailing_list) | **POST** /lists/{MailingListID}/update.{Format} | Updating a mailing list


# **creating_a_custom_field**
> CreatingACustomFieldResponse creating_a_custom_field(format, apikey, mailing_list_id, body)

Creating a custom field

Creates a new custom field in the specified mailing list.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.MailingListsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
mailing_list_id = 'mailing_list_id_example' # str | The ID of the mailing list where the custom field will belong.
body = Moosend.Wrappers.PythonWrapper.CreatingACustomFieldRequest() # CreatingACustomFieldRequest | 

try: 
    # Creating a custom field
    api_response = api_instance.creating_a_custom_field(format, apikey, mailing_list_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailingListsApi->creating_a_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **mailing_list_id** | **str**| The ID of the mailing list where the custom field will belong. | 
 **body** | [**CreatingACustomFieldRequest**](CreatingACustomFieldRequest.md)|  | 

### Return type

[**CreatingACustomFieldResponse**](CreatingACustomFieldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **creating_a_mailing_list**
> CreatingAMailingListResponse creating_a_mailing_list(format, apikey, body)

Creating a mailing list

Creates a new empty mailing list in your account.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.MailingListsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
body = Moosend.Wrappers.PythonWrapper.CreatingAMailingListRequest() # CreatingAMailingListRequest | 

try: 
    # Creating a mailing list
    api_response = api_instance.creating_a_mailing_list(format, apikey, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailingListsApi->creating_a_mailing_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **body** | [**CreatingAMailingListRequest**](CreatingAMailingListRequest.md)|  | 

### Return type

[**CreatingAMailingListResponse**](CreatingAMailingListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleting_a_mailing_list**
> DeletingAMailingListResponse deleting_a_mailing_list(format, apikey, mailing_list_id)

Deleting a mailing list

Deletes a mailing list from your account.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.MailingListsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
mailing_list_id = 'mailing_list_id_example' # str | The ID of the mailing list to be deleted.

try: 
    # Deleting a mailing list
    api_response = api_instance.deleting_a_mailing_list(format, apikey, mailing_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailingListsApi->deleting_a_mailing_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **mailing_list_id** | **str**| The ID of the mailing list to be deleted. | 

### Return type

[**DeletingAMailingListResponse**](DeletingAMailingListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getting_all_active_mailing_lists**
> GettingAllActiveMailingListsResponse getting_all_active_mailing_lists(format, apikey, with_statistics=with_statistics, short_by=short_by, sort_method=sort_method)

Getting all active mailing lists

Gets a list of your active mailing lists in your account.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.MailingListsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
with_statistics = 'with_statistics_example' # str | Specifies whether to fetch statistics for the subscribers or not. If omitted, results will be returned with statistics by default. (optional)
short_by = 'short_by_example' # str | The name of the campaign property to sort results by. If not specified, results will be sorted by the CreatedOn property (optional)
sort_method = 'sort_method_example' # str | The method to sort results: ASC for ascending, DESC for descending. If not specified, `ASC` will be assumed (optional)

try: 
    # Getting all active mailing lists
    api_response = api_instance.getting_all_active_mailing_lists(format, apikey, with_statistics=with_statistics, short_by=short_by, sort_method=sort_method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailingListsApi->getting_all_active_mailing_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **with_statistics** | **str**| Specifies whether to fetch statistics for the subscribers or not. If omitted, results will be returned with statistics by default. | [optional] 
 **short_by** | **str**| The name of the campaign property to sort results by. If not specified, results will be sorted by the CreatedOn property | [optional] 
 **sort_method** | **str**| The method to sort results: ASC for ascending, DESC for descending. If not specified, &#x60;ASC&#x60; will be assumed | [optional] 

### Return type

[**GettingAllActiveMailingListsResponse**](GettingAllActiveMailingListsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getting_all_active_mailing_lists_with_paging**
> GettingAllActiveMailingListsWithPagingResponse getting_all_active_mailing_lists_with_paging(format, apikey, page, page_size, short_by=short_by, sort_method=sort_method)

Getting all active mailing lists with paging

Gets a list of your active mailing lists in your account. Because the results for this call could be quite big, paging information is required as input.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.MailingListsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
page = 1.2 # float | The page that you want to get.
page_size = 1.2 # float | Lists Per Page.
short_by = 'short_by_example' # str | The name of the campaign property to sort results by. If not specified, results will be sorted by the CreatedOn property (optional)
sort_method = 'sort_method_example' # str | The method to sort results: ASC for ascending, DESC for descending. If not specified, `ASC` will be assumed (optional)

try: 
    # Getting all active mailing lists with paging
    api_response = api_instance.getting_all_active_mailing_lists_with_paging(format, apikey, page, page_size, short_by=short_by, sort_method=sort_method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailingListsApi->getting_all_active_mailing_lists_with_paging: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **page** | **float**| The page that you want to get. | 
 **page_size** | **float**| Lists Per Page. | 
 **short_by** | **str**| The name of the campaign property to sort results by. If not specified, results will be sorted by the CreatedOn property | [optional] 
 **sort_method** | **str**| The method to sort results: ASC for ascending, DESC for descending. If not specified, &#x60;ASC&#x60; will be assumed | [optional] 

### Return type

[**GettingAllActiveMailingListsWithPagingResponse**](GettingAllActiveMailingListsWithPagingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getting_mailing_list_details**
> GettingMailingListDetailsResponse getting_mailing_list_details(format, mailing_list_id, apikey, with_statistics=with_statistics)

Getting mailing list details

Gets details for a given mailing list. You may include subscriber statistics in your results or not. Any segments existing for the requested mailing list will not be included in the results.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.MailingListsApi()
format = 'format_example' # str | 
mailing_list_id = 'mailing_list_id_example' # str | The ID of the mailing list to be returned.
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
with_statistics = 'with_statistics_example' # str | Specifies whether to fetch statistics for the subscribers or not. If omitted, results will be returned with statistics by default. (optional)

try: 
    # Getting mailing list details
    api_response = api_instance.getting_mailing_list_details(format, mailing_list_id, apikey, with_statistics=with_statistics)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailingListsApi->getting_mailing_list_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **mailing_list_id** | **str**| The ID of the mailing list to be returned. | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **with_statistics** | **str**| Specifies whether to fetch statistics for the subscribers or not. If omitted, results will be returned with statistics by default. | [optional] 

### Return type

[**GettingMailingListDetailsResponse**](GettingMailingListDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **removing_a_custom_field**
> RemovingACustomFieldResponse removing_a_custom_field(format, custom_field_id, apikey, mailing_list_id)

Removing a custom field

Removes a custom field definition from the specified mailing list.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.MailingListsApi()
format = 'format_example' # str | 
custom_field_id = 'custom_field_id_example' # str | The ID of the custom field to be deleted.
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
mailing_list_id = 'mailing_list_id_example' # str | The ID of the mailing list where the custom field belongs.

try: 
    # Removing a custom field
    api_response = api_instance.removing_a_custom_field(format, custom_field_id, apikey, mailing_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailingListsApi->removing_a_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **custom_field_id** | **str**| The ID of the custom field to be deleted. | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **mailing_list_id** | **str**| The ID of the mailing list where the custom field belongs. | 

### Return type

[**RemovingACustomFieldResponse**](RemovingACustomFieldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updating_a_custom_field**
> UpdatingACustomFieldResponse updating_a_custom_field(format, custom_field_id, apikey, mailing_list_id, body)

Updating a custom field

Updates the properties of an existing custom field in the specified mailing list.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.MailingListsApi()
format = 'format_example' # str | 
custom_field_id = 'custom_field_id_example' # str | The ID of the custom field to be updated.
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
mailing_list_id = 'mailing_list_id_example' # str | The ID of the mailing list where the custom field belongs.
body = Moosend.Wrappers.PythonWrapper.UpdatingACustomFieldRequest() # UpdatingACustomFieldRequest | 

try: 
    # Updating a custom field
    api_response = api_instance.updating_a_custom_field(format, custom_field_id, apikey, mailing_list_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailingListsApi->updating_a_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **custom_field_id** | **str**| The ID of the custom field to be updated. | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **mailing_list_id** | **str**| The ID of the mailing list where the custom field belongs. | 
 **body** | [**UpdatingACustomFieldRequest**](UpdatingACustomFieldRequest.md)|  | 

### Return type

[**UpdatingACustomFieldResponse**](UpdatingACustomFieldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updating_a_mailing_list**
> UpdatingAMailingListResponse updating_a_mailing_list(format, apikey, mailing_list_id, body)

Updating a mailing list

Updates the properties of an existing mailing list.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.MailingListsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
mailing_list_id = 'mailing_list_id_example' # str | The ID of the mailing list to be updated.
body = Moosend.Wrappers.PythonWrapper.UpdatingAMailingListRequest() # UpdatingAMailingListRequest | 

try: 
    # Updating a mailing list
    api_response = api_instance.updating_a_mailing_list(format, apikey, mailing_list_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailingListsApi->updating_a_mailing_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **mailing_list_id** | **str**| The ID of the mailing list to be updated. | 
 **body** | [**UpdatingAMailingListRequest**](UpdatingAMailingListRequest.md)|  | 

### Return type

[**UpdatingAMailingListResponse**](UpdatingAMailingListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

