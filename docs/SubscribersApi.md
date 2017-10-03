# Moosend.Wrappers.PythonWrapper.SubscribersApi

All URIs are relative to *https://api.moosend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adding_multiple_subscribers**](SubscribersApi.md#adding_multiple_subscribers) | **POST** /subscribers/{MailingListID}/subscribe_many.{Format} | Adding multiple subscribers
[**adding_subscribers**](SubscribersApi.md#adding_subscribers) | **POST** /subscribers/{MailingListID}/subscribe.{Format} | Adding subscribers
[**get_subscriber_by_email_address**](SubscribersApi.md#get_subscriber_by_email_address) | **GET** /subscribers/{MailingListID}/view.{Format} | Get subscriber by email address
[**get_subscriber_by_id**](SubscribersApi.md#get_subscriber_by_id) | **GET** /subscribers/{MailingListID}/find/{SubscriberID}.{Format} | Get subscriber by id
[**getting_subscribers**](SubscribersApi.md#getting_subscribers) | **GET** /lists/{MailingListID}/subscribers/{Status}.{Format} | Getting subscribers
[**removing_a_subscriber**](SubscribersApi.md#removing_a_subscriber) | **POST** /subscribers/{MailingListID}/remove.{Format} | Removing a subscriber
[**removing_multiple_subscribers**](SubscribersApi.md#removing_multiple_subscribers) | **POST** /subscribers/{MailingListID}/remove_many.{Format} | Removing multiple subscribers
[**unsubscribing_subscribers_from_account**](SubscribersApi.md#unsubscribing_subscribers_from_account) | **POST** /subscribers/unsubscribe.{Format} | Unsubscribing subscribers from account
[**unsubscribing_subscribers_from_mailing_list**](SubscribersApi.md#unsubscribing_subscribers_from_mailing_list) | **POST** /subscribers/{MailingListID}/unsubscribe.{Format} | Unsubscribing subscribers from mailing list
[**unsubscribing_subscribers_from_mailing_list_and_a_specified_campaign**](SubscribersApi.md#unsubscribing_subscribers_from_mailing_list_and_a_specified_campaign) | **POST** /subscribers/{MailingListID}/{CampaignID}/unsubscribe.{Format} | Unsubscribing subscribers from mailing list and a specified campaign
[**updating_a_subscriber**](SubscribersApi.md#updating_a_subscriber) | **POST** /subscribers/{MailingListID}/update/{SubscriberID}.{Format} | Updating a subscriber


# **adding_multiple_subscribers**
> AddingMultipleSubscribersResponse adding_multiple_subscribers(format, apikey, mailing_list_id, body)

Adding multiple subscribers

This method allows you to add multiple subscribers in a mailing list with a single call. If some subscribers already exist with the given email addresses, they will be updated. If you try to add a subscriber with an invalid email address, this attempt will be ignored, as the process will skip to the next subscriber automatically.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.SubscribersApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
mailing_list_id = 'mailing_list_id_example' # str | The ID of the mailing list to add subscribers to.
body = Moosend.Wrappers.PythonWrapper.AddingMultipleSubscribersRequest() # AddingMultipleSubscribersRequest | 

try: 
    # Adding multiple subscribers
    api_response = api_instance.adding_multiple_subscribers(format, apikey, mailing_list_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->adding_multiple_subscribers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **mailing_list_id** | **str**| The ID of the mailing list to add subscribers to. | 
 **body** | [**AddingMultipleSubscribersRequest**](AddingMultipleSubscribersRequest.md)|  | 

### Return type

[**AddingMultipleSubscribersResponse**](AddingMultipleSubscribersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adding_subscribers**
> AddingSubscribersResponse adding_subscribers(format, mailing_list_id, apikey, body)

Adding subscribers

Adds a new subscriber to the specified mailing list. If there is already a subscriber with the specified email address in the list, an update will be performed instead.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.SubscribersApi()
format = 'format_example' # str | 
mailing_list_id = 'mailing_list_id_example' # str | The ID of the mailing list to add the new member.
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
body = Moosend.Wrappers.PythonWrapper.AddingSubscribersRequest() # AddingSubscribersRequest | 

try: 
    # Adding subscribers
    api_response = api_instance.adding_subscribers(format, mailing_list_id, apikey, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->adding_subscribers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **mailing_list_id** | **str**| The ID of the mailing list to add the new member. | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **body** | [**AddingSubscribersRequest**](AddingSubscribersRequest.md)|  | 

### Return type

[**AddingSubscribersResponse**](AddingSubscribersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriber_by_email_address**
> GetSubscriberByEmailAddressResponse get_subscriber_by_email_address(format, apikey, mailing_list_id, email)

Get subscriber by email address

Searches for a subscriber with the specified email address in the specified mailing list and returns detailed information such as id, name, date created, date unsubscribed, status and custom fields

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.SubscribersApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
mailing_list_id = 'mailing_list_id_example' # str | The ID of the mailing list where the subscriber belongs.
email = 'email_example' # str | The email of the subscriber.

try: 
    # Get subscriber by email address
    api_response = api_instance.get_subscriber_by_email_address(format, apikey, mailing_list_id, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->get_subscriber_by_email_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **mailing_list_id** | **str**| The ID of the mailing list where the subscriber belongs. | 
 **email** | **str**| The email of the subscriber. | 

### Return type

[**GetSubscriberByEmailAddressResponse**](GetSubscriberByEmailAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriber_by_id**
> GetSubscriberByIdResponse get_subscriber_by_id(format, apikey, mailing_list_id, subscriber_id)

Get subscriber by id

Searches for a subscriber with the specified unique id in the specified mailing list and returns detailed information such as email, name, date created, date unsubscribed, status and custom fields.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.SubscribersApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
mailing_list_id = 'mailing_list_id_example' # str | The ID of the mailing list to search the subscriber in.
subscriber_id = 'subscriber_id_example' # str | The id of the subscriber being searched.

try: 
    # Get subscriber by id
    api_response = api_instance.get_subscriber_by_id(format, apikey, mailing_list_id, subscriber_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->get_subscriber_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **mailing_list_id** | **str**| The ID of the mailing list to search the subscriber in. | 
 **subscriber_id** | **str**| The id of the subscriber being searched. | 

### Return type

[**GetSubscriberByIdResponse**](GetSubscriberByIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getting_subscribers**
> GettingSubscribersResponse getting_subscribers(format, mailing_list_id, apikey, status, page=page, page_size=page_size)

Getting subscribers

Gets a list of all subscribers in a given mailing list. You may filter the list by setting a date to fetch those subscribed since then and/or by their status. Because the results for this call could be quite big, paging information is required as input.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.SubscribersApi()
format = 'format_example' # str | 
mailing_list_id = 'mailing_list_id_example' # str | The ID of the mailing list where the subscribers belong.
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
status = 'status_example' # str | Specifies what type of subscriber statistics results will be returned.
page = 1.2 # float | Specifies the page of subscriber statistics results will be returned. (optional)
page_size = 1.2 # float | Specifies the page size of subscriber statistics results will be returned. (optional)

try: 
    # Getting subscribers
    api_response = api_instance.getting_subscribers(format, mailing_list_id, apikey, status, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->getting_subscribers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **mailing_list_id** | **str**| The ID of the mailing list where the subscribers belong. | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **status** | **str**| Specifies what type of subscriber statistics results will be returned. | 
 **page** | **float**| Specifies the page of subscriber statistics results will be returned. | [optional] 
 **page_size** | **float**| Specifies the page size of subscriber statistics results will be returned. | [optional] 

### Return type

[**GettingSubscribersResponse**](GettingSubscribersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **removing_a_subscriber**
> RemovingASubscriberResponse removing_a_subscriber(format, apikey, mailing_list_id, body)

Removing a subscriber

Removes a subscriber from the specified mailing list permanently (without moving to the suppression list).

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.SubscribersApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
mailing_list_id = 'mailing_list_id_example' # str | The ID of the mailing list to remove the subscriber from.
body = Moosend.Wrappers.PythonWrapper.RemovingASubscriberRequest() # RemovingASubscriberRequest | 

try: 
    # Removing a subscriber
    api_response = api_instance.removing_a_subscriber(format, apikey, mailing_list_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->removing_a_subscriber: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **mailing_list_id** | **str**| The ID of the mailing list to remove the subscriber from. | 
 **body** | [**RemovingASubscriberRequest**](RemovingASubscriberRequest.md)|  | 

### Return type

[**RemovingASubscriberResponse**](RemovingASubscriberResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **removing_multiple_subscribers**
> RemovingMultipleSubscribersResponse removing_multiple_subscribers(format, apikey, mailing_list_id, body)

Removing multiple subscribers

Removes a list of subscribers from the specified mailing list permanently (without putting them in the suppression list). Any invalid email addresses specified will be ignored.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.SubscribersApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
mailing_list_id = 'mailing_list_id_example' # str | The ID of the mailing list to remove the subscribers from.
body = Moosend.Wrappers.PythonWrapper.RemovingMultipleSubscribersRequest() # RemovingMultipleSubscribersRequest | 

try: 
    # Removing multiple subscribers
    api_response = api_instance.removing_multiple_subscribers(format, apikey, mailing_list_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->removing_multiple_subscribers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **mailing_list_id** | **str**| The ID of the mailing list to remove the subscribers from. | 
 **body** | [**RemovingMultipleSubscribersRequest**](RemovingMultipleSubscribersRequest.md)|  | 

### Return type

[**RemovingMultipleSubscribersResponse**](RemovingMultipleSubscribersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribing_subscribers_from_account**
> UnsubscribingSubscribersFromAccountResponse unsubscribing_subscribers_from_account(format, apikey, body)

Unsubscribing subscribers from account

Unsubscribes a subscriber from the account.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.SubscribersApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
body = Moosend.Wrappers.PythonWrapper.UnsubscribingSubscribersFromAccountRequest() # UnsubscribingSubscribersFromAccountRequest | 

try: 
    # Unsubscribing subscribers from account
    api_response = api_instance.unsubscribing_subscribers_from_account(format, apikey, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->unsubscribing_subscribers_from_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **body** | [**UnsubscribingSubscribersFromAccountRequest**](UnsubscribingSubscribersFromAccountRequest.md)|  | 

### Return type

[**UnsubscribingSubscribersFromAccountResponse**](UnsubscribingSubscribersFromAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribing_subscribers_from_mailing_list**
> UnsubscribingSubscribersFromMailingListResponse unsubscribing_subscribers_from_mailing_list(format, apikey, mailing_list_id, body)

Unsubscribing subscribers from mailing list

Unsubscribes a subscriber from the specified mailing list. The subscriber is not deleted, but moved to the suppression list.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.SubscribersApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
mailing_list_id = 'mailing_list_id_example' # str | The ID of the mailing list to add subscribers to.
body = Moosend.Wrappers.PythonWrapper.UnsubscribingSubscribersFromMailingListRequest() # UnsubscribingSubscribersFromMailingListRequest | 

try: 
    # Unsubscribing subscribers from mailing list
    api_response = api_instance.unsubscribing_subscribers_from_mailing_list(format, apikey, mailing_list_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->unsubscribing_subscribers_from_mailing_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **mailing_list_id** | **str**| The ID of the mailing list to add subscribers to. | 
 **body** | [**UnsubscribingSubscribersFromMailingListRequest**](UnsubscribingSubscribersFromMailingListRequest.md)|  | 

### Return type

[**UnsubscribingSubscribersFromMailingListResponse**](UnsubscribingSubscribersFromMailingListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribing_subscribers_from_mailing_list_and_a_specified_campaign**
> UnsubscribingSubscribersFromMailingListAndASpecifiedCampaignResponse unsubscribing_subscribers_from_mailing_list_and_a_specified_campaign(format, campaign_id, apikey, mailing_list_id, body)

Unsubscribing subscribers from mailing list and a specified campaign

Unsubscribes a subscriber from the specified mailing list and the specified campaign. The subscriber is not deleted, but moved to the suppression list.  This call will take into account the setting you have in \"suppression list and unsubscribe settings\" and will remove the subscriber from all other mailing lists or not accordingly.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.SubscribersApi()
format = 'format_example' # str | 
campaign_id = 'campaign_id_example' # str | The ID of the campaign that was sent to the specific mailing list.
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
mailing_list_id = 'mailing_list_id_example' # str | The ID of the mailing list to remove the subscriber from.
body = Moosend.Wrappers.PythonWrapper.UnsubscribingSubscribersFromMailingListAndASpecifiedCampaignRequest() # UnsubscribingSubscribersFromMailingListAndASpecifiedCampaignRequest | 

try: 
    # Unsubscribing subscribers from mailing list and a specified campaign
    api_response = api_instance.unsubscribing_subscribers_from_mailing_list_and_a_specified_campaign(format, campaign_id, apikey, mailing_list_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->unsubscribing_subscribers_from_mailing_list_and_a_specified_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **campaign_id** | **str**| The ID of the campaign that was sent to the specific mailing list. | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **mailing_list_id** | **str**| The ID of the mailing list to remove the subscriber from. | 
 **body** | [**UnsubscribingSubscribersFromMailingListAndASpecifiedCampaignRequest**](UnsubscribingSubscribersFromMailingListAndASpecifiedCampaignRequest.md)|  | 

### Return type

[**UnsubscribingSubscribersFromMailingListAndASpecifiedCampaignResponse**](UnsubscribingSubscribersFromMailingListAndASpecifiedCampaignResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updating_a_subscriber**
> UpdatingASubscriberResponse updating_a_subscriber(format, apikey, mailing_list_id, subscriber_id, body)

Updating a subscriber

Updates a subscriber in the specified mailing list. You can even update the subscribers email, if he has not unsubscribed.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.SubscribersApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
mailing_list_id = 'mailing_list_id_example' # str | The ID of the mailing list that contains the subscriber
subscriber_id = 'subscriber_id_example' # str | The id of the subscriber to be updated
body = Moosend.Wrappers.PythonWrapper.UpdatingASubscriberRequest() # UpdatingASubscriberRequest | 

try: 
    # Updating a subscriber
    api_response = api_instance.updating_a_subscriber(format, apikey, mailing_list_id, subscriber_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->updating_a_subscriber: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **mailing_list_id** | **str**| The ID of the mailing list that contains the subscriber | 
 **subscriber_id** | **str**| The id of the subscriber to be updated | 
 **body** | [**UpdatingASubscriberRequest**](UpdatingASubscriberRequest.md)|  | 

### Return type

[**UpdatingASubscriberResponse**](UpdatingASubscriberResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

