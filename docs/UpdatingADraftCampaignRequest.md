# UpdatingADraftCampaignRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the campaign. | [optional] 
**subject** | **str** | The subject line of the new campaign. | [optional] 
**sender_email** | **str** | The sender email of the campaign. | [optional] 
**reply_to_email** | **str** | The email address to which recipients replies will arrive. It must be one of your sender accounts. If not specified, the sender&#39;s email will be assumed. | [optional] 
**is_ab** | **str** | A flag that defines if a campaign is an AB campaign. | [optional] 
**confirmation_to_email** | **str** | The email address to which a confirmation message will be,  sent when the campaign has been successfully sent. | [optional] 
**web_location** | **str** | A url to retrieve the html content for the campaign. We&#39;ll automatically move all CSS inline. | [optional] 
**mailing_lists** | [**list[MailingLists]**](MailingLists.md) | A list of mailing lists in your account to which the campaign will be sent to. | [optional] 
**segment_id** | **str** | The ID of a segment in the specified mailing list to filter the recipients with. If not specified, the campaign will be sent to all active subscribers of the mailing list. | [optional] 
**ab_campaign_type** | **str** | If you want to send an AB split campaign you should specify this parameter to one of the following values.  * &#x60;Subject&#x60; * &#x60;Sender&#x60; * &#x60;Content&#x60; | [optional] 
**track_in_google_analytics** | **str** | Tracks traffic from your campaign to your site. Note: You need to have Google Analytics configured on your site to use this feature. | [optional] 
**dont_track_link_clicks** | **str** | Moosend wraps your own links with its own to enable link click tracking. Check this box if you don&#39;t wish to track link click traffic through Moosend. | [optional] 
**subject_b** | **str** | If you wish to send an AB split campaign with two different versions of the subject line , you must specify the second subject using this parameter. If specified in any other campaign type, it will be ignored. | [optional] 
**web_location_b** | **str** | If you wish to send an AB split campaign with two different versions of the html content, you must specify where the second html content will be retrieved from using this parameter. If specified in any other campaign type, it will be ignored. | [optional] 
**sender_email_b** | **str** | If you wish to send an AB split campaign with two different versions of the sender , you must specify the second sender email address using this parameter. This must be one of your sender signatures defined in your account. If specified in any other campaign type, it will be ignored. | [optional] 
**hours_to_test** | **str** | If you choose to send an AB campaign type, you must set this parameter to specify how long the test will run, before determining which will be the winning version to be sent to the rest of the recipients. This should be an integer value between 1 and 24. If specified in a regular campaign, it will be ignored. | [optional] 
**list_percentage** | **str** | If you choose to send an AB campaign type, you must set this parameter to specify a portion of the target recipients that will receive the test versions. For example, if you specify 10, then 10% of your recipients will receive the A version and another 10% will receive the B version. The specified value should be an integer between 5 and 40. If specified in a regular campaign, it will be ignored. (optional, string) | [optional] 
**ab_winner_selection_type** | **str** | If you choose to send an AB campaign type, you may set this parameter to one of the following values to specify the method to determine the winning version for the test.   If not set, OpenRate will be assumed. If specified in a regular campaign, it will be ignored. * &#x60;OpenRate&#x60; * &#x60;TotalUniqueClicks&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


