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


class RemovingMultipleSubscribersResponse(object):
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
        'code': 'float',
        'context': 'Context64',
        'error': 'str'
    }

    attribute_map = {
        'code': 'Code',
        'context': 'Context',
        'error': 'Error'
    }

    def __init__(self, code=None, context=None, error=None):
        """
        RemovingMultipleSubscribersResponse - a model defined in Swagger
        """

        self._code = None
        self._context = None
        self._error = None

        if code is not None:
          self.code = code
        if context is not None:
          self.context = context
        if error is not None:
          self.error = error

    @property
    def code(self):
        """
        Gets the code of this RemovingMultipleSubscribersResponse.
        

        :return: The code of this RemovingMultipleSubscribersResponse.
        :rtype: float
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this RemovingMultipleSubscribersResponse.
        

        :param code: The code of this RemovingMultipleSubscribersResponse.
        :type: float
        """

        self._code = code

    @property
    def context(self):
        """
        Gets the context of this RemovingMultipleSubscribersResponse.

        :return: The context of this RemovingMultipleSubscribersResponse.
        :rtype: Context64
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this RemovingMultipleSubscribersResponse.

        :param context: The context of this RemovingMultipleSubscribersResponse.
        :type: Context64
        """

        self._context = context

    @property
    def error(self):
        """
        Gets the error of this RemovingMultipleSubscribersResponse.
        

        :return: The error of this RemovingMultipleSubscribersResponse.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this RemovingMultipleSubscribersResponse.
        

        :param error: The error of this RemovingMultipleSubscribersResponse.
        :type: str
        """

        self._error = error

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
        if not isinstance(other, RemovingMultipleSubscribersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
