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


class UnsubscribingSubscribersFromMailingListResponse(object):
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
        'code': 'int',
        'error': 'str',
        'context': 'str'
    }

    attribute_map = {
        'code': 'Code',
        'error': 'Error',
        'context': 'Context'
    }

    def __init__(self, code=None, error=None, context=None):
        """
        UnsubscribingSubscribersFromMailingListResponse - a model defined in Swagger
        """

        self._code = None
        self._error = None
        self._context = None

        self.code = code
        self.error = error
        self.context = context

    @property
    def code(self):
        """
        Gets the code of this UnsubscribingSubscribersFromMailingListResponse.
        

        :return: The code of this UnsubscribingSubscribersFromMailingListResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this UnsubscribingSubscribersFromMailingListResponse.
        

        :param code: The code of this UnsubscribingSubscribersFromMailingListResponse.
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def error(self):
        """
        Gets the error of this UnsubscribingSubscribersFromMailingListResponse.
        

        :return: The error of this UnsubscribingSubscribersFromMailingListResponse.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this UnsubscribingSubscribersFromMailingListResponse.
        

        :param error: The error of this UnsubscribingSubscribersFromMailingListResponse.
        :type: str
        """
        if error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")

        self._error = error

    @property
    def context(self):
        """
        Gets the context of this UnsubscribingSubscribersFromMailingListResponse.
        

        :return: The context of this UnsubscribingSubscribersFromMailingListResponse.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this UnsubscribingSubscribersFromMailingListResponse.
        

        :param context: The context of this UnsubscribingSubscribersFromMailingListResponse.
        :type: str
        """
        if context is None:
            raise ValueError("Invalid value for `context`, must not be `None`")

        self._context = context

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
        if not isinstance(other, UnsubscribingSubscribersFromMailingListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
