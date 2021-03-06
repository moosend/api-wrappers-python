# coding: utf-8

"""
    Moosend API

    TODO: Add a description

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CreatingADraftCampaignRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'subject': 'str',
        'sender_email': 'str',
        'reply_to_email': 'str',
        'is_ab': 'str',
        'confirmation_to_email': 'str',
        'web_location': 'str',
        'mailing_lists': 'list[MailingLists]',
        'segment_id': 'str',
        'ab_campaign_type': 'str',
        'track_in_google_analytics': 'str',
        'dont_track_link_clicks': 'str',
        'subject_b': 'str',
        'web_location_b': 'str',
        'sender_email_b': 'str',
        'hours_to_test': 'str',
        'list_percentage': 'str',
        'ab_winner_selection_type': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'subject': 'Subject',
        'sender_email': 'SenderEmail',
        'reply_to_email': 'ReplyToEmail',
        'is_ab': 'IsAB',
        'confirmation_to_email': 'ConfirmationToEmail',
        'web_location': 'WebLocation',
        'mailing_lists': 'MailingLists',
        'segment_id': 'SegmentID',
        'ab_campaign_type': 'ABCampaignType',
        'track_in_google_analytics': 'TrackInGoogleAnalytics',
        'dont_track_link_clicks': 'DontTrackLinkClicks',
        'subject_b': 'SubjectB',
        'web_location_b': 'WebLocationB',
        'sender_email_b': 'SenderEmailB',
        'hours_to_test': 'HoursToTest',
        'list_percentage': 'ListPercentage',
        'ab_winner_selection_type': 'ABWinnerSelectionType'
    }

    def __init__(self, name=None, subject=None, sender_email=None, reply_to_email=None, is_ab=None, confirmation_to_email=None, web_location=None, mailing_lists=None, segment_id=None, ab_campaign_type=None, track_in_google_analytics=None, dont_track_link_clicks=None, subject_b=None, web_location_b=None, sender_email_b=None, hours_to_test=None, list_percentage=None, ab_winner_selection_type=None):
        """
        CreatingADraftCampaignRequest - a model defined in Swagger
        """

        self._name = None
        self._subject = None
        self._sender_email = None
        self._reply_to_email = None
        self._is_ab = None
        self._confirmation_to_email = None
        self._web_location = None
        self._mailing_lists = None
        self._segment_id = None
        self._ab_campaign_type = None
        self._track_in_google_analytics = None
        self._dont_track_link_clicks = None
        self._subject_b = None
        self._web_location_b = None
        self._sender_email_b = None
        self._hours_to_test = None
        self._list_percentage = None
        self._ab_winner_selection_type = None

        self.name = name
        self.subject = subject
        self.sender_email = sender_email
        self.reply_to_email = reply_to_email
        self.is_ab = is_ab
        if confirmation_to_email is not None:
          self.confirmation_to_email = confirmation_to_email
        if web_location is not None:
          self.web_location = web_location
        if mailing_lists is not None:
          self.mailing_lists = mailing_lists
        if segment_id is not None:
          self.segment_id = segment_id
        if ab_campaign_type is not None:
          self.ab_campaign_type = ab_campaign_type
        if track_in_google_analytics is not None:
          self.track_in_google_analytics = track_in_google_analytics
        if dont_track_link_clicks is not None:
          self.dont_track_link_clicks = dont_track_link_clicks
        if subject_b is not None:
          self.subject_b = subject_b
        if web_location_b is not None:
          self.web_location_b = web_location_b
        if sender_email_b is not None:
          self.sender_email_b = sender_email_b
        if hours_to_test is not None:
          self.hours_to_test = hours_to_test
        if list_percentage is not None:
          self.list_percentage = list_percentage
        if ab_winner_selection_type is not None:
          self.ab_winner_selection_type = ab_winner_selection_type

    @property
    def name(self):
        """
        Gets the name of this CreatingADraftCampaignRequest.
        The name of the campaign.

        :return: The name of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreatingADraftCampaignRequest.
        The name of the campaign.

        :param name: The name of this CreatingADraftCampaignRequest.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def subject(self):
        """
        Gets the subject of this CreatingADraftCampaignRequest.
        The subject line of the new campaign.

        :return: The subject of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this CreatingADraftCampaignRequest.
        The subject line of the new campaign.

        :param subject: The subject of this CreatingADraftCampaignRequest.
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")

        self._subject = subject

    @property
    def sender_email(self):
        """
        Gets the sender_email of this CreatingADraftCampaignRequest.
        The sender email of the campaign.

        :return: The sender_email of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._sender_email

    @sender_email.setter
    def sender_email(self, sender_email):
        """
        Sets the sender_email of this CreatingADraftCampaignRequest.
        The sender email of the campaign.

        :param sender_email: The sender_email of this CreatingADraftCampaignRequest.
        :type: str
        """
        if sender_email is None:
            raise ValueError("Invalid value for `sender_email`, must not be `None`")

        self._sender_email = sender_email

    @property
    def reply_to_email(self):
        """
        Gets the reply_to_email of this CreatingADraftCampaignRequest.
        The email address to which recipients replies will arrive. It must be one of your sender accounts. If not specified, the sender's email will be assumed.

        :return: The reply_to_email of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._reply_to_email

    @reply_to_email.setter
    def reply_to_email(self, reply_to_email):
        """
        Sets the reply_to_email of this CreatingADraftCampaignRequest.
        The email address to which recipients replies will arrive. It must be one of your sender accounts. If not specified, the sender's email will be assumed.

        :param reply_to_email: The reply_to_email of this CreatingADraftCampaignRequest.
        :type: str
        """
        if reply_to_email is None:
            raise ValueError("Invalid value for `reply_to_email`, must not be `None`")

        self._reply_to_email = reply_to_email

    @property
    def is_ab(self):
        """
        Gets the is_ab of this CreatingADraftCampaignRequest.
        A flag that defines if a campaign is an AB campaign.

        :return: The is_ab of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._is_ab

    @is_ab.setter
    def is_ab(self, is_ab):
        """
        Sets the is_ab of this CreatingADraftCampaignRequest.
        A flag that defines if a campaign is an AB campaign.

        :param is_ab: The is_ab of this CreatingADraftCampaignRequest.
        :type: str
        """
        if is_ab is None:
            raise ValueError("Invalid value for `is_ab`, must not be `None`")

        self._is_ab = is_ab

    @property
    def confirmation_to_email(self):
        """
        Gets the confirmation_to_email of this CreatingADraftCampaignRequest.
        The email address to which a confirmation message will be,  sent when the campaign has been successfully sent.

        :return: The confirmation_to_email of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._confirmation_to_email

    @confirmation_to_email.setter
    def confirmation_to_email(self, confirmation_to_email):
        """
        Sets the confirmation_to_email of this CreatingADraftCampaignRequest.
        The email address to which a confirmation message will be,  sent when the campaign has been successfully sent.

        :param confirmation_to_email: The confirmation_to_email of this CreatingADraftCampaignRequest.
        :type: str
        """

        self._confirmation_to_email = confirmation_to_email

    @property
    def web_location(self):
        """
        Gets the web_location of this CreatingADraftCampaignRequest.
        A url to retrieve the html content for the campaign. We'll automatically move all CSS inline.

        :return: The web_location of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._web_location

    @web_location.setter
    def web_location(self, web_location):
        """
        Sets the web_location of this CreatingADraftCampaignRequest.
        A url to retrieve the html content for the campaign. We'll automatically move all CSS inline.

        :param web_location: The web_location of this CreatingADraftCampaignRequest.
        :type: str
        """

        self._web_location = web_location

    @property
    def mailing_lists(self):
        """
        Gets the mailing_lists of this CreatingADraftCampaignRequest.
        A list of mailing lists in your account to which the campaign will be sent to.

        :return: The mailing_lists of this CreatingADraftCampaignRequest.
        :rtype: list[MailingLists]
        """
        return self._mailing_lists

    @mailing_lists.setter
    def mailing_lists(self, mailing_lists):
        """
        Sets the mailing_lists of this CreatingADraftCampaignRequest.
        A list of mailing lists in your account to which the campaign will be sent to.

        :param mailing_lists: The mailing_lists of this CreatingADraftCampaignRequest.
        :type: list[MailingLists]
        """

        self._mailing_lists = mailing_lists

    @property
    def segment_id(self):
        """
        Gets the segment_id of this CreatingADraftCampaignRequest.
        The ID of a segment in the specified mailing list to filter the recipients with. If not specified, the campaign will be sent to all active subscribers of the mailing list.

        :return: The segment_id of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id):
        """
        Sets the segment_id of this CreatingADraftCampaignRequest.
        The ID of a segment in the specified mailing list to filter the recipients with. If not specified, the campaign will be sent to all active subscribers of the mailing list.

        :param segment_id: The segment_id of this CreatingADraftCampaignRequest.
        :type: str
        """

        self._segment_id = segment_id

    @property
    def ab_campaign_type(self):
        """
        Gets the ab_campaign_type of this CreatingADraftCampaignRequest.
        If you want to send an AB split campaign you should specify this parameter to one of the following values.  * `Subject` * `Sender` * `Content`

        :return: The ab_campaign_type of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._ab_campaign_type

    @ab_campaign_type.setter
    def ab_campaign_type(self, ab_campaign_type):
        """
        Sets the ab_campaign_type of this CreatingADraftCampaignRequest.
        If you want to send an AB split campaign you should specify this parameter to one of the following values.  * `Subject` * `Sender` * `Content`

        :param ab_campaign_type: The ab_campaign_type of this CreatingADraftCampaignRequest.
        :type: str
        """

        self._ab_campaign_type = ab_campaign_type

    @property
    def track_in_google_analytics(self):
        """
        Gets the track_in_google_analytics of this CreatingADraftCampaignRequest.
        Tracks traffic from your campaign to your site. Note: You need to have Google Analytics configured on your site to use this feature.

        :return: The track_in_google_analytics of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._track_in_google_analytics

    @track_in_google_analytics.setter
    def track_in_google_analytics(self, track_in_google_analytics):
        """
        Sets the track_in_google_analytics of this CreatingADraftCampaignRequest.
        Tracks traffic from your campaign to your site. Note: You need to have Google Analytics configured on your site to use this feature.

        :param track_in_google_analytics: The track_in_google_analytics of this CreatingADraftCampaignRequest.
        :type: str
        """

        self._track_in_google_analytics = track_in_google_analytics

    @property
    def dont_track_link_clicks(self):
        """
        Gets the dont_track_link_clicks of this CreatingADraftCampaignRequest.
        Moosend wraps your own links with its own to enable link click tracking. Check this box if you don't wish to track link click traffic through Moosend.

        :return: The dont_track_link_clicks of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._dont_track_link_clicks

    @dont_track_link_clicks.setter
    def dont_track_link_clicks(self, dont_track_link_clicks):
        """
        Sets the dont_track_link_clicks of this CreatingADraftCampaignRequest.
        Moosend wraps your own links with its own to enable link click tracking. Check this box if you don't wish to track link click traffic through Moosend.

        :param dont_track_link_clicks: The dont_track_link_clicks of this CreatingADraftCampaignRequest.
        :type: str
        """

        self._dont_track_link_clicks = dont_track_link_clicks

    @property
    def subject_b(self):
        """
        Gets the subject_b of this CreatingADraftCampaignRequest.
        If you wish to send an AB split campaign with two different versions of the subject line , you must specify the second subject using this parameter. If specified in any other campaign type, it will be ignored.

        :return: The subject_b of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._subject_b

    @subject_b.setter
    def subject_b(self, subject_b):
        """
        Sets the subject_b of this CreatingADraftCampaignRequest.
        If you wish to send an AB split campaign with two different versions of the subject line , you must specify the second subject using this parameter. If specified in any other campaign type, it will be ignored.

        :param subject_b: The subject_b of this CreatingADraftCampaignRequest.
        :type: str
        """

        self._subject_b = subject_b

    @property
    def web_location_b(self):
        """
        Gets the web_location_b of this CreatingADraftCampaignRequest.
        If you wish to send an AB split campaign with two different versions of the html content, you must specify where the second html content will be retrieved from using this parameter. If specified in any other campaign type, it will be ignored.

        :return: The web_location_b of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._web_location_b

    @web_location_b.setter
    def web_location_b(self, web_location_b):
        """
        Sets the web_location_b of this CreatingADraftCampaignRequest.
        If you wish to send an AB split campaign with two different versions of the html content, you must specify where the second html content will be retrieved from using this parameter. If specified in any other campaign type, it will be ignored.

        :param web_location_b: The web_location_b of this CreatingADraftCampaignRequest.
        :type: str
        """

        self._web_location_b = web_location_b

    @property
    def sender_email_b(self):
        """
        Gets the sender_email_b of this CreatingADraftCampaignRequest.
        If you wish to send an AB split campaign with two different versions of the sender , you must specify the second sender email address using this parameter. This must be one of your sender signatures defined in your account. If specified in any other campaign type, it will be ignored.

        :return: The sender_email_b of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._sender_email_b

    @sender_email_b.setter
    def sender_email_b(self, sender_email_b):
        """
        Sets the sender_email_b of this CreatingADraftCampaignRequest.
        If you wish to send an AB split campaign with two different versions of the sender , you must specify the second sender email address using this parameter. This must be one of your sender signatures defined in your account. If specified in any other campaign type, it will be ignored.

        :param sender_email_b: The sender_email_b of this CreatingADraftCampaignRequest.
        :type: str
        """

        self._sender_email_b = sender_email_b

    @property
    def hours_to_test(self):
        """
        Gets the hours_to_test of this CreatingADraftCampaignRequest.
        If you choose to send an AB campaign type, you must set this parameter to specify how long the test will run, before determining which will be the winning version to be sent to the rest of the recipients. This should be an integer value between 1 and 24. If specified in a regular campaign, it will be ignored.

        :return: The hours_to_test of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._hours_to_test

    @hours_to_test.setter
    def hours_to_test(self, hours_to_test):
        """
        Sets the hours_to_test of this CreatingADraftCampaignRequest.
        If you choose to send an AB campaign type, you must set this parameter to specify how long the test will run, before determining which will be the winning version to be sent to the rest of the recipients. This should be an integer value between 1 and 24. If specified in a regular campaign, it will be ignored.

        :param hours_to_test: The hours_to_test of this CreatingADraftCampaignRequest.
        :type: str
        """

        self._hours_to_test = hours_to_test

    @property
    def list_percentage(self):
        """
        Gets the list_percentage of this CreatingADraftCampaignRequest.
        If you choose to send an AB campaign type, you must set this parameter to specify a portion of the target recipients that will receive the test versions. For example, if you specify 10, then 10% of your recipients will receive the A version and another 10% will receive the B version. The specified value should be an integer between 5 and 40. If specified in a regular campaign, it will be ignored. (optional, string)

        :return: The list_percentage of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._list_percentage

    @list_percentage.setter
    def list_percentage(self, list_percentage):
        """
        Sets the list_percentage of this CreatingADraftCampaignRequest.
        If you choose to send an AB campaign type, you must set this parameter to specify a portion of the target recipients that will receive the test versions. For example, if you specify 10, then 10% of your recipients will receive the A version and another 10% will receive the B version. The specified value should be an integer between 5 and 40. If specified in a regular campaign, it will be ignored. (optional, string)

        :param list_percentage: The list_percentage of this CreatingADraftCampaignRequest.
        :type: str
        """

        self._list_percentage = list_percentage

    @property
    def ab_winner_selection_type(self):
        """
        Gets the ab_winner_selection_type of this CreatingADraftCampaignRequest.
        If you choose to send an AB campaign type, you may set this parameter to one of the following values to specify the method to determine the winning version for the test.   If not set, OpenRate will be assumed. If specified in a regular campaign, it will be ignored. * `OpenRate` * `TotalUniqueClicks`

        :return: The ab_winner_selection_type of this CreatingADraftCampaignRequest.
        :rtype: str
        """
        return self._ab_winner_selection_type

    @ab_winner_selection_type.setter
    def ab_winner_selection_type(self, ab_winner_selection_type):
        """
        Sets the ab_winner_selection_type of this CreatingADraftCampaignRequest.
        If you choose to send an AB campaign type, you may set this parameter to one of the following values to specify the method to determine the winning version for the test.   If not set, OpenRate will be assumed. If specified in a regular campaign, it will be ignored. * `OpenRate` * `TotalUniqueClicks`

        :param ab_winner_selection_type: The ab_winner_selection_type of this CreatingADraftCampaignRequest.
        :type: str
        """

        self._ab_winner_selection_type = ab_winner_selection_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CreatingADraftCampaignRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
