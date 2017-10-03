# Moosend Python Wrapper

The following project is a Python implementation of the Moosend V3 API.
You can find the API documentation at http://docs.moosendapp.apiary.io/#

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install git+https://github.com/moosend/api-wrappers-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/moosend/api-wrappers-python.git`)

Then import the package:
```python
import moosend_api_wrapper
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import moosend_api_wrapper
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import Moosend.Wrappers.CSharpWrapper
from Moosend.Wrappers.CSharpWrapper.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = Moosend.Wrappers.CSharpWrapper.CampaignsApi()
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

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

## *CampaignsApi*
Class | Method 
------------ | ------------- 
[**GetAllCampaigns**](docs/CampaignsApi.md#getallcampaigns) | Returns a list of all campaigns in your account with detailed information.  
[**GetCampaignsByPage**](docs/CampaignsApi.md#getcampaignsbypage) | Returns a list of all campaigns in your account with detailed information, paging information is required as input.
[**GetCampaignsByPageAndPagesize**](docs/CampaignsApi.md#getcampaignsbypageandpagesize) | Returns a list of all campaigns in your account with detailed information, paging information is required as input.
[**GettingCampaignDetails**](docs/CampaignsApi.md#gettingcampaigndetails) | Returns a complete set of properties that describe the requested campaign in detail.  
[**GettingSenderDetails**](docs/CampaignsApi.md#gettingsenderdetails) | Returns basic information for the specified sender identified by its email address.
[**CloningAnExistingCampaign**](docs/CampaignsApi.md#cloninganexistingcampaign) | Creates an exact copy of an existing campaign. The new campaign is created as a draft.
[**CreatingADraftCampaign**](docs/CampaignsApi.md#creatingadraftcampaign) | Creates a new campaign in your account. This method does not send the campaign, but rather creates it as a draft, ready for sending or testing. 
[**UpdatingADraftCampaign**](docs/CampaignsApi.md#updatingadraftcampaign) | Updates properties of an existing draft A/B campaign in your account. Non-draft campaigns cannot be updated. 
[**DeletingACampaign**](docs/CampaignsApi.md#deletingacampaign) | Deletes a campaign from your account, draft or even sent.
[**TestingACampaign**](docs/CampaignsApi.md#testingacampaign) | Sends a test email of a draft campaign to a list of email addresses you specify for previewing.
[**SendingACampaign**](docs/CampaignsApi.md#sendingacampaign) | Sends an existing draft campaign to all recipients specified in its mailing list. The campaign is sent immediatelly.
[**ABTestCampaignSummary**](docs/CampaignsApi.md#abtestcampaignsummary) |  Provides a basic summary of the results for a sent AB test campaign, separately for each version (A and B), such as the number of recipients, opens, clicks, bounces, unsubscribes, forwards etc to date.
[**ActivityByLocation**](docs/CampaignsApi.md#activitybylocation) |  Returns a detailed report of your campaign opens (unique and total) by country.
[**CampaignSummary**](docs/CampaignsApi.md#campaignsummary) | Provides a basic summary of the results for any sent campaign such as the number of recipients, opens, clicks, bounces, unsubscribes, forwards etc. to date.
[**GettingAllYourSenders**](docs/CampaignsApi.md#gettingallyoursenders) | Gets a list of your active senders in your account. You may specify any email address of these senders when sending a campaign.
[**LinkActivity**](docs/CampaignsApi.md#linkactivity) | Returns a list with your campaign links and how many clicks have been made by your recipients, either unique or total.
[**SchedulingACampaign**](docs/CampaignsApi.md#schedulingacampaign) | Assigns a scheduled date and time at which the campaign will be delivered.
[**UnschedulingACampaign**](docs/CampaignsApi.md#unschedulingacampaign) | Removes a previously defined scheduled date and time from a campaign, so that it will be delivered immediately if already queued or when sent.

## *MailingListsApi*
Class | Method 
------------ | ------------- 
[**CreatingACustomField**](docs/MailingListsApi.md#creatingacustomfield) | Creates a new custom field in the specified mailing list.
[**CreatingAMailingList**](docs/MailingListsApi.md#creatingamailinglist) | Creates a new empty mailing list in your account.
[**DeletingAMailingList**](docs/MailingListsApi.md#deletingamailinglist) | Deletes a mailing list from your account.
[**GettingAllActiveMailingLists**](docs/MailingListsApi.md#gettingallactivemailinglists) | Gets a list of your active mailing lists in your account.
[**GettingAllActiveMailingListsWithPaging**](docs/MailingListsApi.md#gettingallactivemailinglistswithpaging) | Gets a list of your active mailing lists in your account. Because the results for this call could be quite big, paging information is required as input.
[**GettingMailingListDetails**](docs/MailingListsApi.md#gettingmailinglistdetails) | Gets details for a given mailing list. You may include subscriber statistics in your results or not. Any segments existing for the requested mailing list will not be included in the results.
[**RemovingACustomField**](docs/MailingListsApi.md#removingacustomfield) | Removes a custom field definition from the specified mailing list.
[**UpdatingACustomField**](docs/MailingListsApi.md#updatingacustomfield) | Updates the properties of an existing custom field in the specified mailing list.
[**UpdatingAMailingList**](docs/MailingListsApi.md#updatingamailinglist) | Updates the properties of an existing mailing list.

## *SegmentsApi*
Class | Method 
------------ | ------------- 
[**GettingSegments**](docs/SegmentsApi.md#gettingsegments) | Get a list of all segments with their criteria for the given mailing list.
[**GettingSegmentDetails**](docs/SegmentsApi.md#gettingsegmentdetails) | Gets detailed information on a specific segment and its criteria. However, it does not include the subscribers returned by the segment.
[**GettingSegmentSubscribers**](docs/SegmentsApi.md#gettingsegmentsubscribers) | Gets a list of the subscribers that the specified segment returns according to its criteria. Because the results for this call could be quite big, paging information is required as input.
[**CreatingANewSegment**](docs/SegmentsApi.md#creatinganewsegment) | Creates a new empty segment (without criteria) for the given mailing list. You may specify the name of the segment and the way the criteria will match together.
[**UpdatingASegment**](docs/SegmentsApi.md#updatingasegment) | Updates the properties of an existing segment. You may update the name and match type of the segment.
[**AddingCriteriaToSegments**](docs/SegmentsApi.md#addingcriteriatosegments) | Adds a new criterion (a rule) to the specified segment.
[**UpdatingSegmentCriteria**](docs/SegmentsApi.md#updatingsegmentcriteria) | Updates an existing criterion in the specified segment.
[**DeletingASegment**](docs/SegmentsApi.md#deletingasegment) | Deletes a segment along with its criteria from the mailing list. The subscribers of the mailing list that the segment returned are not deleted or affected in any way.

## *SubscribersApi*
Class | Method 
------------ | ------------- 
[**GettingSubscribers**](docs/SubscribersApi.md#gettingsubscribers) | Gets a list of all subscribers in a given mailing list. You may filter the list by setting a date to fetch those subscribed since then and/or by their status. 
[**GetSubscriberByEmailAddress**](docs/SubscribersApi.md#getsubscriberbyemailaddress) | Searches for a subscriber with the specified email address in the specified mailing list.
[**GetSubscriberById**](docs/SubscribersApi.md#getsubscriberbyid) | Searches for a subscriber with the specified unique id in the specified mailing list
[**AddingSubscribers**](docs/SubscribersApi.md#addingsubscribers) | Adds a new subscriber to the specified mailing list. If there is already a subscriber with the specified email address in the list, an update will be performed instead.
[**AddingMultipleSubscribers**](docs/SubscribersApi.md#addingmultiplesubscribers) | This method allows you to add multiple subscribers in a mailing list with a single call. If some subscribers already exist with the given email addresses, they will be updated. 
[**UpdatingASubscriber**](docs/SubscribersApi.md#updatingasubscriber) | Updates a subscriber in the specified mailing list. You can even update the subscribers email, if he has not unsubscribed.
[**UnsubscribingSubscribersFromAccount**](docs/SubscribersApi.md#unsubscribingsubscribersfromaccount) | Unsubscribes a subscriber from the account.
[**UnsubscribingSubscribersFromMailingList**](docs/SubscribersApi.md#unsubscribingsubscribersfrommailinglist) | Unsubscribes a subscriber from the specified mailing list. The subscriber is not deleted, but moved to the suppression list.
[**UnsubscribingSubscribersFromMailingListAndASpecifiedCampaign**](docs/SubscribersApi.md#unsubscribingsubscribersfrommailinglistandaspecifiedcampaign) | Unsubscribes a subscriber from the specified mailing list and the specified campaign. The subscriber is not deleted, but moved to the suppression list. 
[**RemovingASubscriber**](docs/SubscribersApi.md#removingasubscriber) | Removes a subscriber from the specified mailing list permanently (without moving to the suppression list).
[**RemovingMultipleSubscribers**](docs/SubscribersApi.md#removingmultiplesubscribers) | Removes a list of subscribers from the specified mailing list permanently (without putting them in the suppression list). Any invalid email addresses specified will be ignored.


## Documentation For Models

 - [A](docs/A.md)
 - [ABCampaignData](docs/ABCampaignData.md)
 - [AbTestCampaignSummaryResponse](docs/AbTestCampaignSummaryResponse.md)
 - [ActivityByLocationResponse](docs/ActivityByLocationResponse.md)
 - [AddingCriteriaToSegmentsRequest](docs/AddingCriteriaToSegmentsRequest.md)
 - [AddingCriteriaToSegmentsResponse](docs/AddingCriteriaToSegmentsResponse.md)
 - [AddingMultipleSubscribersRequest](docs/AddingMultipleSubscribersRequest.md)
 - [AddingMultipleSubscribersResponse](docs/AddingMultipleSubscribersResponse.md)
 - [AddingSubscribersRequest](docs/AddingSubscribersRequest.md)
 - [AddingSubscribersResponse](docs/AddingSubscribersResponse.md)
 - [Analytic](docs/Analytic.md)
 - [B](docs/B.md)
 - [Campaign](docs/Campaign.md)
 - [CampaignSummaryResponse](docs/CampaignSummaryResponse.md)
 - [CloningAnExistingCampaignResponse](docs/CloningAnExistingCampaignResponse.md)
 - [Context](docs/Context.md)
 - [Context110](docs/Context110.md)
 - [Context118](docs/Context118.md)
 - [Context132](docs/Context132.md)
 - [Context140](docs/Context140.md)
 - [Context145](docs/Context145.md)
 - [Context148](docs/Context148.md)
 - [Context17](docs/Context17.md)
 - [Context32](docs/Context32.md)
 - [Context37](docs/Context37.md)
 - [Context52](docs/Context52.md)
 - [Context64](docs/Context64.md)
 - [Context66](docs/Context66.md)
 - [Context72](docs/Context72.md)
 - [Context84](docs/Context84.md)
 - [Context89](docs/Context89.md)
 - [Context93](docs/Context93.md)
 - [CreatingACustomFieldRequest](docs/CreatingACustomFieldRequest.md)
 - [CreatingACustomFieldResponse](docs/CreatingACustomFieldResponse.md)
 - [CreatingADraftCampaignRequest](docs/CreatingADraftCampaignRequest.md)
 - [CreatingADraftCampaignResponse](docs/CreatingADraftCampaignResponse.md)
 - [CreatingAMailingListRequest](docs/CreatingAMailingListRequest.md)
 - [CreatingAMailingListResponse](docs/CreatingAMailingListResponse.md)
 - [CreatingANewSegmentRequest](docs/CreatingANewSegmentRequest.md)
 - [CreatingANewSegmentResponse](docs/CreatingANewSegmentResponse.md)
 - [Criterion](docs/Criterion.md)
 - [CustomField](docs/CustomField.md)
 - [CustomField53](docs/CustomField53.md)
 - [CustomFieldsDefinition](docs/CustomFieldsDefinition.md)
 - [DeletingACampaignResponse](docs/DeletingACampaignResponse.md)
 - [DeletingAMailingListResponse](docs/DeletingAMailingListResponse.md)
 - [DeletingASegmentResponse](docs/DeletingASegmentResponse.md)
 - [Format](docs/Format.md)
 - [GetAllCampaignsResponse](docs/GetAllCampaignsResponse.md)
 - [GetCampaignStatisticsResponse](docs/GetCampaignStatisticsResponse.md)
 - [GetCampaignStatisticsWithPagingFilteredResponse](docs/GetCampaignStatisticsWithPagingFilteredResponse.md)
 - [GetCampaignsByPageAndPagesizeResponse](docs/GetCampaignsByPageAndPagesizeResponse.md)
 - [GetCampaignsByPageResponse](docs/GetCampaignsByPageResponse.md)
 - [GetSubscriberByEmailAddressResponse](docs/GetSubscriberByEmailAddressResponse.md)
 - [GetSubscriberByIdResponse](docs/GetSubscriberByIdResponse.md)
 - [GettingAllActiveMailingListsResponse](docs/GettingAllActiveMailingListsResponse.md)
 - [GettingAllActiveMailingListsWithPagingResponse](docs/GettingAllActiveMailingListsWithPagingResponse.md)
 - [GettingAllYourSendersResponse](docs/GettingAllYourSendersResponse.md)
 - [GettingCampaignDetailsResponse](docs/GettingCampaignDetailsResponse.md)
 - [GettingMailingListDetailsResponse](docs/GettingMailingListDetailsResponse.md)
 - [GettingSegmentDetailsResponse](docs/GettingSegmentDetailsResponse.md)
 - [GettingSegmentSubscribersResponse](docs/GettingSegmentSubscribersResponse.md)
 - [GettingSegmentsResponse](docs/GettingSegmentsResponse.md)
 - [GettingSenderDetailsResponse](docs/GettingSenderDetailsResponse.md)
 - [GettingSubscribersResponse](docs/GettingSubscribersResponse.md)
 - [ImportOperation](docs/ImportOperation.md)
 - [ImportOperation19](docs/ImportOperation19.md)
 - [LinkActivityResponse](docs/LinkActivityResponse.md)
 - [MailingList](docs/MailingList.md)
 - [MailingList68](docs/MailingList68.md)
 - [MailingList69](docs/MailingList69.md)
 - [MailingList85](docs/MailingList85.md)
 - [MailingLists](docs/MailingLists.md)
 - [MailingLists119](docs/MailingLists119.md)
 - [MailingLists134](docs/MailingLists134.md)
 - [Paging](docs/Paging.md)
 - [Paging76](docs/Paging76.md)
 - [RemovingACustomFieldResponse](docs/RemovingACustomFieldResponse.md)
 - [RemovingASubscriberRequest](docs/RemovingASubscriberRequest.md)
 - [RemovingASubscriberResponse](docs/RemovingASubscriberResponse.md)
 - [RemovingMultipleSubscribersRequest](docs/RemovingMultipleSubscribersRequest.md)
 - [RemovingMultipleSubscribersResponse](docs/RemovingMultipleSubscribersResponse.md)
 - [ReplyToEmail](docs/ReplyToEmail.md)
 - [SchedulingACampaignRequest](docs/SchedulingACampaignRequest.md)
 - [SchedulingACampaignResponse](docs/SchedulingACampaignResponse.md)
 - [Segment](docs/Segment.md)
 - [Sender](docs/Sender.md)
 - [SendingACampaignResponse](docs/SendingACampaignResponse.md)
 - [ShortBy](docs/ShortBy.md)
 - [SortMethod](docs/SortMethod.md)
 - [Status](docs/Status.md)
 - [Subscriber](docs/Subscriber.md)
 - [Subscribers](docs/Subscribers.md)
 - [Subscribers150](docs/Subscribers150.md)
 - [TestingACampaignRequest](docs/TestingACampaignRequest.md)
 - [TestingACampaignResponse](docs/TestingACampaignResponse.md)
 - [Type](docs/Type.md)
 - [UnschedulingACampaignResponse](docs/UnschedulingACampaignResponse.md)
 - [UnsubscribingSubscribersFromAccountRequest](docs/UnsubscribingSubscribersFromAccountRequest.md)
 - [UnsubscribingSubscribersFromAccountResponse](docs/UnsubscribingSubscribersFromAccountResponse.md)
 - [UnsubscribingSubscribersFromMailingListAndASpecifiedCampaignRequest](docs/UnsubscribingSubscribersFromMailingListAndASpecifiedCampaignRequest.md)
 - [UnsubscribingSubscribersFromMailingListAndASpecifiedCampaignResponse](docs/UnsubscribingSubscribersFromMailingListAndASpecifiedCampaignResponse.md)
 - [UnsubscribingSubscribersFromMailingListRequest](docs/UnsubscribingSubscribersFromMailingListRequest.md)
 - [UnsubscribingSubscribersFromMailingListResponse](docs/UnsubscribingSubscribersFromMailingListResponse.md)
 - [UpdatingACustomFieldRequest](docs/UpdatingACustomFieldRequest.md)
 - [UpdatingACustomFieldResponse](docs/UpdatingACustomFieldResponse.md)
 - [UpdatingADraftCampaignRequest](docs/UpdatingADraftCampaignRequest.md)
 - [UpdatingADraftCampaignResponse](docs/UpdatingADraftCampaignResponse.md)
 - [UpdatingAMailingListRequest](docs/UpdatingAMailingListRequest.md)
 - [UpdatingAMailingListResponse](docs/UpdatingAMailingListResponse.md)
 - [UpdatingASegmentRequest](docs/UpdatingASegmentRequest.md)
 - [UpdatingASegmentResponse](docs/UpdatingASegmentResponse.md)
 - [UpdatingASubscriberRequest](docs/UpdatingASubscriberRequest.md)
 - [UpdatingASubscriberResponse](docs/UpdatingASubscriberResponse.md)
 - [UpdatingSegmentCriteriaRequest](docs/UpdatingSegmentCriteriaRequest.md)
 - [UpdatingSegmentCriteriaResponse](docs/UpdatingSegmentCriteriaResponse.md)
 - [WithStatistics](docs/WithStatistics.md)



