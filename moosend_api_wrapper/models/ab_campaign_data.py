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


class ABCampaignData(object):
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
        'ab_campaign_type': 'float',
        'ab_winner_selection_type': 'float',
        'delivered_on_a': 'str',
        'delivered_on_b': 'str',
        'html_content_b': 'str',
        'hours_to_test': 'float',
        'id': 'float',
        'list_percentage': 'float',
        'plain_content_b': 'str',
        'sender_b': 'str',
        'subject_b': 'str',
        'web_location_b': 'str'
    }

    attribute_map = {
        'ab_campaign_type': 'ABCampaignType',
        'ab_winner_selection_type': 'ABWinnerSelectionType',
        'delivered_on_a': 'DeliveredOnA',
        'delivered_on_b': 'DeliveredOnB',
        'html_content_b': 'HTMLContentB',
        'hours_to_test': 'HoursToTest',
        'id': 'ID',
        'list_percentage': 'ListPercentage',
        'plain_content_b': 'PlainContentB',
        'sender_b': 'SenderB',
        'subject_b': 'SubjectB',
        'web_location_b': 'WebLocationB'
    }

    def __init__(self, ab_campaign_type=None, ab_winner_selection_type=None, delivered_on_a=None, delivered_on_b=None, html_content_b=None, hours_to_test=None, id=None, list_percentage=None, plain_content_b=None, sender_b=None, subject_b=None, web_location_b=None):
        """
        ABCampaignData - a model defined in Swagger
        """

        self._ab_campaign_type = None
        self._ab_winner_selection_type = None
        self._delivered_on_a = None
        self._delivered_on_b = None
        self._html_content_b = None
        self._hours_to_test = None
        self._id = None
        self._list_percentage = None
        self._plain_content_b = None
        self._sender_b = None
        self._subject_b = None
        self._web_location_b = None

        if ab_campaign_type is not None:
          self.ab_campaign_type = ab_campaign_type
        if ab_winner_selection_type is not None:
          self.ab_winner_selection_type = ab_winner_selection_type
        if delivered_on_a is not None:
          self.delivered_on_a = delivered_on_a
        if delivered_on_b is not None:
          self.delivered_on_b = delivered_on_b
        if html_content_b is not None:
          self.html_content_b = html_content_b
        if hours_to_test is not None:
          self.hours_to_test = hours_to_test
        if id is not None:
          self.id = id
        if list_percentage is not None:
          self.list_percentage = list_percentage
        if plain_content_b is not None:
          self.plain_content_b = plain_content_b
        if sender_b is not None:
          self.sender_b = sender_b
        if subject_b is not None:
          self.subject_b = subject_b
        if web_location_b is not None:
          self.web_location_b = web_location_b

    @property
    def ab_campaign_type(self):
        """
        Gets the ab_campaign_type of this ABCampaignData.
        

        :return: The ab_campaign_type of this ABCampaignData.
        :rtype: float
        """
        return self._ab_campaign_type

    @ab_campaign_type.setter
    def ab_campaign_type(self, ab_campaign_type):
        """
        Sets the ab_campaign_type of this ABCampaignData.
        

        :param ab_campaign_type: The ab_campaign_type of this ABCampaignData.
        :type: float
        """

        self._ab_campaign_type = ab_campaign_type

    @property
    def ab_winner_selection_type(self):
        """
        Gets the ab_winner_selection_type of this ABCampaignData.
        

        :return: The ab_winner_selection_type of this ABCampaignData.
        :rtype: float
        """
        return self._ab_winner_selection_type

    @ab_winner_selection_type.setter
    def ab_winner_selection_type(self, ab_winner_selection_type):
        """
        Sets the ab_winner_selection_type of this ABCampaignData.
        

        :param ab_winner_selection_type: The ab_winner_selection_type of this ABCampaignData.
        :type: float
        """

        self._ab_winner_selection_type = ab_winner_selection_type

    @property
    def delivered_on_a(self):
        """
        Gets the delivered_on_a of this ABCampaignData.
        

        :return: The delivered_on_a of this ABCampaignData.
        :rtype: str
        """
        return self._delivered_on_a

    @delivered_on_a.setter
    def delivered_on_a(self, delivered_on_a):
        """
        Sets the delivered_on_a of this ABCampaignData.
        

        :param delivered_on_a: The delivered_on_a of this ABCampaignData.
        :type: str
        """

        self._delivered_on_a = delivered_on_a

    @property
    def delivered_on_b(self):
        """
        Gets the delivered_on_b of this ABCampaignData.
        

        :return: The delivered_on_b of this ABCampaignData.
        :rtype: str
        """
        return self._delivered_on_b

    @delivered_on_b.setter
    def delivered_on_b(self, delivered_on_b):
        """
        Sets the delivered_on_b of this ABCampaignData.
        

        :param delivered_on_b: The delivered_on_b of this ABCampaignData.
        :type: str
        """

        self._delivered_on_b = delivered_on_b

    @property
    def html_content_b(self):
        """
        Gets the html_content_b of this ABCampaignData.
        

        :return: The html_content_b of this ABCampaignData.
        :rtype: str
        """
        return self._html_content_b

    @html_content_b.setter
    def html_content_b(self, html_content_b):
        """
        Sets the html_content_b of this ABCampaignData.
        

        :param html_content_b: The html_content_b of this ABCampaignData.
        :type: str
        """

        self._html_content_b = html_content_b

    @property
    def hours_to_test(self):
        """
        Gets the hours_to_test of this ABCampaignData.
        

        :return: The hours_to_test of this ABCampaignData.
        :rtype: float
        """
        return self._hours_to_test

    @hours_to_test.setter
    def hours_to_test(self, hours_to_test):
        """
        Sets the hours_to_test of this ABCampaignData.
        

        :param hours_to_test: The hours_to_test of this ABCampaignData.
        :type: float
        """

        self._hours_to_test = hours_to_test

    @property
    def id(self):
        """
        Gets the id of this ABCampaignData.
        

        :return: The id of this ABCampaignData.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ABCampaignData.
        

        :param id: The id of this ABCampaignData.
        :type: float
        """

        self._id = id

    @property
    def list_percentage(self):
        """
        Gets the list_percentage of this ABCampaignData.
        

        :return: The list_percentage of this ABCampaignData.
        :rtype: float
        """
        return self._list_percentage

    @list_percentage.setter
    def list_percentage(self, list_percentage):
        """
        Sets the list_percentage of this ABCampaignData.
        

        :param list_percentage: The list_percentage of this ABCampaignData.
        :type: float
        """

        self._list_percentage = list_percentage

    @property
    def plain_content_b(self):
        """
        Gets the plain_content_b of this ABCampaignData.
        

        :return: The plain_content_b of this ABCampaignData.
        :rtype: str
        """
        return self._plain_content_b

    @plain_content_b.setter
    def plain_content_b(self, plain_content_b):
        """
        Sets the plain_content_b of this ABCampaignData.
        

        :param plain_content_b: The plain_content_b of this ABCampaignData.
        :type: str
        """

        self._plain_content_b = plain_content_b

    @property
    def sender_b(self):
        """
        Gets the sender_b of this ABCampaignData.
        

        :return: The sender_b of this ABCampaignData.
        :rtype: str
        """
        return self._sender_b

    @sender_b.setter
    def sender_b(self, sender_b):
        """
        Sets the sender_b of this ABCampaignData.
        

        :param sender_b: The sender_b of this ABCampaignData.
        :type: str
        """

        self._sender_b = sender_b

    @property
    def subject_b(self):
        """
        Gets the subject_b of this ABCampaignData.
        

        :return: The subject_b of this ABCampaignData.
        :rtype: str
        """
        return self._subject_b

    @subject_b.setter
    def subject_b(self, subject_b):
        """
        Sets the subject_b of this ABCampaignData.
        

        :param subject_b: The subject_b of this ABCampaignData.
        :type: str
        """

        self._subject_b = subject_b

    @property
    def web_location_b(self):
        """
        Gets the web_location_b of this ABCampaignData.
        

        :return: The web_location_b of this ABCampaignData.
        :rtype: str
        """
        return self._web_location_b

    @web_location_b.setter
    def web_location_b(self, web_location_b):
        """
        Sets the web_location_b of this ABCampaignData.
        

        :param web_location_b: The web_location_b of this ABCampaignData.
        :type: str
        """

        self._web_location_b = web_location_b

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
        if not isinstance(other, ABCampaignData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
