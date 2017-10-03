# Moosend.Wrappers.PythonWrapper.CampaignsApi

All URIs are relative to *https://api.moosend.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**a_b_test_campaign_summary**](CampaignsApi.md#a_b_test_campaign_summary) | **GET** /campaigns/{CampaignID}/view_ab_summary.{Format} | AB Test Campaign Summary
[**activity_by_location**](CampaignsApi.md#activity_by_location) | **GET** /campaigns/{CampaignID}/stats/countries.{Format} | Activity By Location
[**campaign_summary**](CampaignsApi.md#campaign_summary) | **GET** /campaigns/{CampaignID}/view_summary.{Format} | Campaign Summary
[**cloning_an_existing_campaign**](CampaignsApi.md#cloning_an_existing_campaign) | **POST** /campaigns/{CampaignID}/clone.{Format} | Cloning An Existing Campaign
[**creating_a_draft_campaign**](CampaignsApi.md#creating_a_draft_campaign) | **POST** /campaigns/create.{Format} | Creating A Draft Campaign
[**deleting_a_campaign**](CampaignsApi.md#deleting_a_campaign) | **DELETE** /campaigns/{CampaignID}/delete.{Format} | Deleting A Campaign
[**get_all_campaigns**](CampaignsApi.md#get_all_campaigns) | **GET** /campaigns.{Format} | Get All Campaigns
[**get_campaign_statistics_with_paging__filtered**](CampaignsApi.md#get_campaign_statistics_with_paging__filtered) | **GET** /campaigns/{CampaignID}/stats/{Type}.{Format} | Get Campaign Statistics With Paging &amp; Filtered
[**get_campaigns_by_page**](CampaignsApi.md#get_campaigns_by_page) | **GET** /campaigns/{Page}.{Format} | Get Campaigns By Page
[**get_campaigns_by_page_and_pagesize**](CampaignsApi.md#get_campaigns_by_page_and_pagesize) | **GET** /campaigns/{Page}/{PageSize}.{Format} | Get Campaigns By Page And Pagesize
[**getting_all_your_senders**](CampaignsApi.md#getting_all_your_senders) | **GET** /senders/find_all.{Format} | Getting All Your Senders
[**getting_campaign_details**](CampaignsApi.md#getting_campaign_details) | **GET** /campaigns/{CampaignID}/view.{Format} | Getting Campaign Details
[**getting_sender_details**](CampaignsApi.md#getting_sender_details) | **GET** /senders/find_one.{Format} | Getting Sender Details
[**link_activity**](CampaignsApi.md#link_activity) | **GET** /campaigns/{CampaignID}/stats/links.{Format} | Link Activity
[**scheduling_a_campaign**](CampaignsApi.md#scheduling_a_campaign) | **POST** /campaigns/{CampaignID}/schedule.{Format} | Scheduling A Campaign
[**sending_a_campaign**](CampaignsApi.md#sending_a_campaign) | **POST** /campaigns/{CampaignID}/send.{Format} | Sending a campaign
[**testing_a_campaign**](CampaignsApi.md#testing_a_campaign) | **POST** /campaigns/{CampaignID}/send_test.{Format} | Testing a campaign
[**unscheduling_a_campaign**](CampaignsApi.md#unscheduling_a_campaign) | **POST** /campaigns/{CampaignID}/unschedule.{Format} | Unscheduling a campaign
[**updating_a_draft_campaign**](CampaignsApi.md#updating_a_draft_campaign) | **POST** /campaigns/{CampaignID}/update.{Format} | Updating A Draft Campaign


# **a_b_test_campaign_summary**
> AbTestCampaignSummaryResponse a_b_test_campaign_summary(format, apikey, campaign_id)

AB Test Campaign Summary

Provides a basic summary of the results for a sent AB test campaign, separately for each version (A and B), such as the number of recipients, opens, clicks, bounces, unsubscribes, forwards etc to date.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
campaign_id = 'campaign_id_example' # str | The ID of the requested AB test campaign

try: 
    # AB Test Campaign Summary
    api_response = api_instance.a_b_test_campaign_summary(format, apikey, campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->a_b_test_campaign_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **campaign_id** | **str**| The ID of the requested AB test campaign | 

### Return type

[**AbTestCampaignSummaryResponse**](AbTestCampaignSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_by_location**
> ActivityByLocationResponse activity_by_location(format, apikey, campaign_id)

Activity By Location

Returns a detailed report of your campaign opens (unique and total) by country.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
campaign_id = 'campaign_id_example' # str | The ID of the requested campaign

try: 
    # Activity By Location
    api_response = api_instance.activity_by_location(format, apikey, campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->activity_by_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **campaign_id** | **str**| The ID of the requested campaign | 

### Return type

[**ActivityByLocationResponse**](ActivityByLocationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **campaign_summary**
> CampaignSummaryResponse campaign_summary(format, apikey, campaign_id)

Campaign Summary

Provides a basic summary of the results for any sent campaign such as the number of recipients, opens, clicks, bounces, unsubscribes, forwards etc. to date.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
campaign_id = 'campaign_id_example' # str | The ID of the requested campaign

try: 
    # Campaign Summary
    api_response = api_instance.campaign_summary(format, apikey, campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->campaign_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **campaign_id** | **str**| The ID of the requested campaign | 

### Return type

[**CampaignSummaryResponse**](CampaignSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cloning_an_existing_campaign**
> CloningAnExistingCampaignResponse cloning_an_existing_campaign(format, campaign_id, apikey)

Cloning An Existing Campaign

Creates an exact copy of an existing campaign. The new campaign is created as a draft.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
campaign_id = 'campaign_id_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.

try: 
    # Cloning An Existing Campaign
    api_response = api_instance.cloning_an_existing_campaign(format, campaign_id, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->cloning_an_existing_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **campaign_id** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 

### Return type

[**CloningAnExistingCampaignResponse**](CloningAnExistingCampaignResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **creating_a_draft_campaign**
> CreatingADraftCampaignResponse creating_a_draft_campaign(format, apikey, body)

Creating A Draft Campaign

Creates a new campaign in your account. This method does not send the campaign, but rather creates it as a draft, ready for sending or testing.  You can choose to send either a regular campaign or an AB split campaign. Campaign content must be specified from a web location.  Ignore ***(A/B Split Campaign Option)*** if you want to create a regular campaign.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
body = Moosend.Wrappers.PythonWrapper.CreatingADraftCampaignRequest() # CreatingADraftCampaignRequest | 

try: 
    # Creating A Draft Campaign
    api_response = api_instance.creating_a_draft_campaign(format, apikey, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->creating_a_draft_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **body** | [**CreatingADraftCampaignRequest**](CreatingADraftCampaignRequest.md)|  | 

### Return type

[**CreatingADraftCampaignResponse**](CreatingADraftCampaignResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleting_a_campaign**
> DeletingACampaignResponse deleting_a_campaign(format, apikey, campaign_id)

Deleting A Campaign

Deletes a campaign from your account, draft or even sent.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
campaign_id = 'campaign_id_example' # str | The ID of the draft campaign to update.

try: 
    # Deleting A Campaign
    api_response = api_instance.deleting_a_campaign(format, apikey, campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->deleting_a_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **campaign_id** | **str**| The ID of the draft campaign to update. | 

### Return type

[**DeletingACampaignResponse**](DeletingACampaignResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_campaigns**
> GetAllCampaignsResponse get_all_campaigns(format, apikey)

Get All Campaigns

Returns a list of all campaigns in your account with detailed information. Because the results for this call could be quite big, paging information is required as input.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.

try: 
    # Get All Campaigns
    api_response = api_instance.get_all_campaigns(format, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->get_all_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 

### Return type

[**GetAllCampaignsResponse**](GetAllCampaignsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_statistics_with_paging__filtered**
> GetCampaignStatisticsWithPagingFilteredResponse get_campaign_statistics_with_paging__filtered(format, apikey, campaign_id, type, page=page, page_size=page_size, _from=_from, to=to)

Get Campaign Statistics With Paging & Filtered

Returns a detailed list of statistics for a given campaign based on activity such as emails sent, opened, bounced, link clicked, etc.  Because the results for this call could be quite big, paging information is required as input.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
campaign_id = 'campaign_id_example' # str | The ID of the requested AB test campaign
type = 'type_example' # str | The type of the activity to display results for. This must be one of the following values : * Sent : To get information about when and to which recipients the campaign was sent. * Opened : To get information about who opened the campaign. * LinkClicked : To get information about who clicked on which link. * Forward : To get information about who forwarded the campaign using the relevant link on the email body and when. * Unsubscribed : To get information about who unsubscribed from the campaign by clicking on the unsubscribe link and when. * Bounced : To get information about which email recipients failed to receive the campaign. If not specified, the value Sent will be used by default.
page = 'page_example' # str | The page number to display results for. If not specified, the first page will be returned. (optional)
page_size = 'page_size_example' # str | The maximum number of results per page. This must be a positive integer up to 100. If not specified, 50 results per page will be returned.  If a value greater than 100 is specified, it will be treated as 100. (optional)
_from = '_from_example' # str | A date value that specifies since when to start returning results. If omitted, results will be returned from the moment the campaign was sent. (optional)
to = 'to_example' # str | A date value that specifies up to when to return results. If omitted, results will be returned up to date. (optional)

try: 
    # Get Campaign Statistics With Paging & Filtered
    api_response = api_instance.get_campaign_statistics_with_paging__filtered(format, apikey, campaign_id, type, page=page, page_size=page_size, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->get_campaign_statistics_with_paging__filtered: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **campaign_id** | **str**| The ID of the requested AB test campaign | 
 **type** | **str**| The type of the activity to display results for. This must be one of the following values : * Sent : To get information about when and to which recipients the campaign was sent. * Opened : To get information about who opened the campaign. * LinkClicked : To get information about who clicked on which link. * Forward : To get information about who forwarded the campaign using the relevant link on the email body and when. * Unsubscribed : To get information about who unsubscribed from the campaign by clicking on the unsubscribe link and when. * Bounced : To get information about which email recipients failed to receive the campaign. If not specified, the value Sent will be used by default. | 
 **page** | **str**| The page number to display results for. If not specified, the first page will be returned. | [optional] 
 **page_size** | **str**| The maximum number of results per page. This must be a positive integer up to 100. If not specified, 50 results per page will be returned.  If a value greater than 100 is specified, it will be treated as 100. | [optional] 
 **_from** | **str**| A date value that specifies since when to start returning results. If omitted, results will be returned from the moment the campaign was sent. | [optional] 
 **to** | **str**| A date value that specifies up to when to return results. If omitted, results will be returned up to date. | [optional] 

### Return type

[**GetCampaignStatisticsWithPagingFilteredResponse**](GetCampaignStatisticsWithPagingFilteredResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaigns_by_page**
> GetCampaignsByPageResponse get_campaigns_by_page(format, apikey, page)

Get Campaigns By Page

Returns a list of all campaigns in your account with detailed information. Because the results for this call could be quite big, paging information is required as input.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
page = 1.2 # float | The page number to display results for.

try: 
    # Get Campaigns By Page
    api_response = api_instance.get_campaigns_by_page(format, apikey, page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->get_campaigns_by_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **page** | **float**| The page number to display results for. | 

### Return type

[**GetCampaignsByPageResponse**](GetCampaignsByPageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaigns_by_page_and_pagesize**
> GetCampaignsByPageAndPagesizeResponse get_campaigns_by_page_and_pagesize(format, apikey, page, page_size, short_by=short_by, sort_method=sort_method)

Get Campaigns By Page And Pagesize

Returns a list of all campaigns in your account with detailed information. Because the results for this call could be quite big, paging information is required as input.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
page = 1.2 # float | The page number to display results for.
page_size = 1.2 # float | The maximum number of results per page.  This must be a positive integer up to 100. If not specified, 50 results per page will be returned.  If a value greater than 100 is specified, it will be treated as 100.
short_by = 'short_by_example' # str | The name of the campaign property to sort results by. If not specified, results will be sorted by the CreatedOn property (optional)
sort_method = 'sort_method_example' # str | The method to sort results: ASC for ascending, DESC for descending. If not specified, `ASC` will be assumed (optional)

try: 
    # Get Campaigns By Page And Pagesize
    api_response = api_instance.get_campaigns_by_page_and_pagesize(format, apikey, page, page_size, short_by=short_by, sort_method=sort_method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->get_campaigns_by_page_and_pagesize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **page** | **float**| The page number to display results for. | 
 **page_size** | **float**| The maximum number of results per page.  This must be a positive integer up to 100. If not specified, 50 results per page will be returned.  If a value greater than 100 is specified, it will be treated as 100. | 
 **short_by** | **str**| The name of the campaign property to sort results by. If not specified, results will be sorted by the CreatedOn property | [optional] 
 **sort_method** | **str**| The method to sort results: ASC for ascending, DESC for descending. If not specified, &#x60;ASC&#x60; will be assumed | [optional] 

### Return type

[**GetCampaignsByPageAndPagesizeResponse**](GetCampaignsByPageAndPagesizeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getting_all_your_senders**
> GettingAllYourSendersResponse getting_all_your_senders(format, apikey)

Getting All Your Senders

Gets a list of your active senders in your account. You may specify any email address of these senders when sending a campaign.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.

try: 
    # Getting All Your Senders
    api_response = api_instance.getting_all_your_senders(format, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->getting_all_your_senders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 

### Return type

[**GettingAllYourSendersResponse**](GettingAllYourSendersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getting_campaign_details**
> GettingCampaignDetailsResponse getting_campaign_details(format, apikey, campaign_id)

Getting Campaign Details

Returns a complete set of properties that describe the requested campaign in detail. No statistics are included in the result.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
campaign_id = 'campaign_id_example' # str | The ID of the requested campaign

try: 
    # Getting Campaign Details
    api_response = api_instance.getting_campaign_details(format, apikey, campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->getting_campaign_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **campaign_id** | **str**| The ID of the requested campaign | 

### Return type

[**GettingCampaignDetailsResponse**](GettingCampaignDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getting_sender_details**
> GettingSenderDetailsResponse getting_sender_details(format, email, apikey)

Getting Sender Details

Returns basic information for the specified sender identified by its email address.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
email = 'email_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.

try: 
    # Getting Sender Details
    api_response = api_instance.getting_sender_details(format, email, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->getting_sender_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **email** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 

### Return type

[**GettingSenderDetailsResponse**](GettingSenderDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_activity**
> LinkActivityResponse link_activity(format, apikey, campaign_id)

Link Activity

Returns a list with your campaign links and how many clicks have been made by your recipients, either unique or total.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
campaign_id = 'campaign_id_example' # str | The ID of the requested campaign

try: 
    # Link Activity
    api_response = api_instance.link_activity(format, apikey, campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->link_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **campaign_id** | **str**| The ID of the requested campaign | 

### Return type

[**LinkActivityResponse**](LinkActivityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduling_a_campaign**
> SchedulingACampaignResponse scheduling_a_campaign(format, apikey, campaign_id, body)

Scheduling A Campaign

Assigns a scheduled date and time at which the campaign will be delivered.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
campaign_id = 'campaign_id_example' # str | The ID of the campaign to be scheduled
body = Moosend.Wrappers.PythonWrapper.SchedulingACampaignRequest() # SchedulingACampaignRequest | 

try: 
    # Scheduling A Campaign
    api_response = api_instance.scheduling_a_campaign(format, apikey, campaign_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->scheduling_a_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **campaign_id** | **str**| The ID of the campaign to be scheduled | 
 **body** | [**SchedulingACampaignRequest**](SchedulingACampaignRequest.md)|  | 

### Return type

[**SchedulingACampaignResponse**](SchedulingACampaignResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sending_a_campaign**
> SendingACampaignResponse sending_a_campaign(format, apikey, campaign_id)

Sending a campaign

Sends an existing draft campaign to all recipients specified in its mailing list. The campaign is sent immediatelly.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
campaign_id = 'campaign_id_example' # str | The ID of the draft campaign to be sent.

try: 
    # Sending a campaign
    api_response = api_instance.sending_a_campaign(format, apikey, campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->sending_a_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **campaign_id** | **str**| The ID of the draft campaign to be sent. | 

### Return type

[**SendingACampaignResponse**](SendingACampaignResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testing_a_campaign**
> TestingACampaignResponse testing_a_campaign(format, apikey, campaign_id, body)

Testing a campaign

Sends a test email of a draft campaign to a list of email addresses you specify for previewing.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
campaign_id = 'campaign_id_example' # str | The ID of the draft campaign to be tested.
body = Moosend.Wrappers.PythonWrapper.TestingACampaignRequest() # TestingACampaignRequest | 

try: 
    # Testing a campaign
    api_response = api_instance.testing_a_campaign(format, apikey, campaign_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->testing_a_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **campaign_id** | **str**| The ID of the draft campaign to be tested. | 
 **body** | [**TestingACampaignRequest**](TestingACampaignRequest.md)|  | 

### Return type

[**TestingACampaignResponse**](TestingACampaignResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unscheduling_a_campaign**
> UnschedulingACampaignResponse unscheduling_a_campaign(format, apikey, campaign_id)

Unscheduling a campaign

Removes a previously defined scheduled date and time from a campaign, so that it will be delivered immediately if already queued or when sent.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
campaign_id = 'campaign_id_example' # str | The ID of the campaign to be scheduled

try: 
    # Unscheduling a campaign
    api_response = api_instance.unscheduling_a_campaign(format, apikey, campaign_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->unscheduling_a_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **campaign_id** | **str**| The ID of the campaign to be scheduled | 

### Return type

[**UnschedulingACampaignResponse**](UnschedulingACampaignResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updating_a_draft_campaign**
> UpdatingADraftCampaignResponse updating_a_draft_campaign(format, apikey, campaign_id, body)

Updating A Draft Campaign

Updates properties of an existing draft A/B campaign in your account. Non-draft campaigns cannot be updated. Ignore ***(A/B Split Campaign Option)*** if you want to create a regular campaign.

### Example 
```python
from __future__ import print_function
import time
import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = Moosend.Wrappers.PythonWrapper.CampaignsApi()
format = 'format_example' # str | 
apikey = 'apikey_example' # str | You may find your API Key or generate a new one in your account settings.
campaign_id = 'campaign_id_example' # str | The ID of the draft campaign to update.
body = Moosend.Wrappers.PythonWrapper.UpdatingADraftCampaignRequest() # UpdatingADraftCampaignRequest | 

try: 
    # Updating A Draft Campaign
    api_response = api_instance.updating_a_draft_campaign(format, apikey, campaign_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->updating_a_draft_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **apikey** | **str**| You may find your API Key or generate a new one in your account settings. | 
 **campaign_id** | **str**| The ID of the draft campaign to update. | 
 **body** | [**UpdatingADraftCampaignRequest**](UpdatingADraftCampaignRequest.md)|  | 

### Return type

[**UpdatingADraftCampaignResponse**](UpdatingADraftCampaignResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

