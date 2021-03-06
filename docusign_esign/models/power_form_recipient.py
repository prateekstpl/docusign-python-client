# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PowerFormRecipient(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'access_code': 'str',
        'access_code_locked': 'str',
        'access_code_required': 'str',
        'email': 'str',
        'email_locked': 'str',
        'id_check_configuration_name': 'str',
        'id_check_required': 'str',
        'name': 'str',
        'recipient_type': 'str',
        'role_name': 'str',
        'routing_order': 'str',
        'template_requires_id_lookup': 'str',
        'user_name_locked': 'str'
    }

    attribute_map = {
        'access_code': 'accessCode',
        'access_code_locked': 'accessCodeLocked',
        'access_code_required': 'accessCodeRequired',
        'email': 'email',
        'email_locked': 'emailLocked',
        'id_check_configuration_name': 'idCheckConfigurationName',
        'id_check_required': 'idCheckRequired',
        'name': 'name',
        'recipient_type': 'recipientType',
        'role_name': 'roleName',
        'routing_order': 'routingOrder',
        'template_requires_id_lookup': 'templateRequiresIdLookup',
        'user_name_locked': 'userNameLocked'
    }

    def __init__(self, access_code=None, access_code_locked=None, access_code_required=None, email=None, email_locked=None, id_check_configuration_name=None, id_check_required=None, name=None, recipient_type=None, role_name=None, routing_order=None, template_requires_id_lookup=None, user_name_locked=None):  # noqa: E501
        """PowerFormRecipient - a model defined in Swagger"""  # noqa: E501

        self._access_code = None
        self._access_code_locked = None
        self._access_code_required = None
        self._email = None
        self._email_locked = None
        self._id_check_configuration_name = None
        self._id_check_required = None
        self._name = None
        self._recipient_type = None
        self._role_name = None
        self._routing_order = None
        self._template_requires_id_lookup = None
        self._user_name_locked = None
        self.discriminator = None

        if access_code is not None:
            self.access_code = access_code
        if access_code_locked is not None:
            self.access_code_locked = access_code_locked
        if access_code_required is not None:
            self.access_code_required = access_code_required
        if email is not None:
            self.email = email
        if email_locked is not None:
            self.email_locked = email_locked
        if id_check_configuration_name is not None:
            self.id_check_configuration_name = id_check_configuration_name
        if id_check_required is not None:
            self.id_check_required = id_check_required
        if name is not None:
            self.name = name
        if recipient_type is not None:
            self.recipient_type = recipient_type
        if role_name is not None:
            self.role_name = role_name
        if routing_order is not None:
            self.routing_order = routing_order
        if template_requires_id_lookup is not None:
            self.template_requires_id_lookup = template_requires_id_lookup
        if user_name_locked is not None:
            self.user_name_locked = user_name_locked

    @property
    def access_code(self):
        """Gets the access_code of this PowerFormRecipient.  # noqa: E501

        If a value is provided, the recipient must enter the value as the access code to view and sign the envelope.   Maximum Length: 50 characters and it must conform to the account's access code format setting.  If blank, but the signer `accessCode` property is set in the envelope, then that value is used.  If blank and the signer `accessCode` property is not set, then the access code is not required.  # noqa: E501

        :return: The access_code of this PowerFormRecipient.  # noqa: E501
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        """Sets the access_code of this PowerFormRecipient.

        If a value is provided, the recipient must enter the value as the access code to view and sign the envelope.   Maximum Length: 50 characters and it must conform to the account's access code format setting.  If blank, but the signer `accessCode` property is set in the envelope, then that value is used.  If blank and the signer `accessCode` property is not set, then the access code is not required.  # noqa: E501

        :param access_code: The access_code of this PowerFormRecipient.  # noqa: E501
        :type: str
        """

        self._access_code = access_code

    @property
    def access_code_locked(self):
        """Gets the access_code_locked of this PowerFormRecipient.  # noqa: E501

          # noqa: E501

        :return: The access_code_locked of this PowerFormRecipient.  # noqa: E501
        :rtype: str
        """
        return self._access_code_locked

    @access_code_locked.setter
    def access_code_locked(self, access_code_locked):
        """Sets the access_code_locked of this PowerFormRecipient.

          # noqa: E501

        :param access_code_locked: The access_code_locked of this PowerFormRecipient.  # noqa: E501
        :type: str
        """

        self._access_code_locked = access_code_locked

    @property
    def access_code_required(self):
        """Gets the access_code_required of this PowerFormRecipient.  # noqa: E501

          # noqa: E501

        :return: The access_code_required of this PowerFormRecipient.  # noqa: E501
        :rtype: str
        """
        return self._access_code_required

    @access_code_required.setter
    def access_code_required(self, access_code_required):
        """Sets the access_code_required of this PowerFormRecipient.

          # noqa: E501

        :param access_code_required: The access_code_required of this PowerFormRecipient.  # noqa: E501
        :type: str
        """

        self._access_code_required = access_code_required

    @property
    def email(self):
        """Gets the email of this PowerFormRecipient.  # noqa: E501

          # noqa: E501

        :return: The email of this PowerFormRecipient.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PowerFormRecipient.

          # noqa: E501

        :param email: The email of this PowerFormRecipient.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def email_locked(self):
        """Gets the email_locked of this PowerFormRecipient.  # noqa: E501

          # noqa: E501

        :return: The email_locked of this PowerFormRecipient.  # noqa: E501
        :rtype: str
        """
        return self._email_locked

    @email_locked.setter
    def email_locked(self, email_locked):
        """Sets the email_locked of this PowerFormRecipient.

          # noqa: E501

        :param email_locked: The email_locked of this PowerFormRecipient.  # noqa: E501
        :type: str
        """

        self._email_locked = email_locked

    @property
    def id_check_configuration_name(self):
        """Gets the id_check_configuration_name of this PowerFormRecipient.  # noqa: E501

        Specifies authentication check by name. The names used here must be the same as the authentication type names used by the account (these name can also be found in the web console sending interface in the Identify list for a recipient,) This overrides any default authentication setting.  *Example*: Your account has ID Check and SMS Authentication available and in the web console Identify list these appear as 'ID Check $' and 'SMS Auth $'. To use ID check in an envelope, the idCheckConfigurationName should be 'ID Check '. If you wanted to use SMS, it would be 'SMS Auth $' and you would need to add you would need to add phone number information to the `smsAuthentication` node.  # noqa: E501

        :return: The id_check_configuration_name of this PowerFormRecipient.  # noqa: E501
        :rtype: str
        """
        return self._id_check_configuration_name

    @id_check_configuration_name.setter
    def id_check_configuration_name(self, id_check_configuration_name):
        """Sets the id_check_configuration_name of this PowerFormRecipient.

        Specifies authentication check by name. The names used here must be the same as the authentication type names used by the account (these name can also be found in the web console sending interface in the Identify list for a recipient,) This overrides any default authentication setting.  *Example*: Your account has ID Check and SMS Authentication available and in the web console Identify list these appear as 'ID Check $' and 'SMS Auth $'. To use ID check in an envelope, the idCheckConfigurationName should be 'ID Check '. If you wanted to use SMS, it would be 'SMS Auth $' and you would need to add you would need to add phone number information to the `smsAuthentication` node.  # noqa: E501

        :param id_check_configuration_name: The id_check_configuration_name of this PowerFormRecipient.  # noqa: E501
        :type: str
        """

        self._id_check_configuration_name = id_check_configuration_name

    @property
    def id_check_required(self):
        """Gets the id_check_required of this PowerFormRecipient.  # noqa: E501

          # noqa: E501

        :return: The id_check_required of this PowerFormRecipient.  # noqa: E501
        :rtype: str
        """
        return self._id_check_required

    @id_check_required.setter
    def id_check_required(self, id_check_required):
        """Sets the id_check_required of this PowerFormRecipient.

          # noqa: E501

        :param id_check_required: The id_check_required of this PowerFormRecipient.  # noqa: E501
        :type: str
        """

        self._id_check_required = id_check_required

    @property
    def name(self):
        """Gets the name of this PowerFormRecipient.  # noqa: E501

          # noqa: E501

        :return: The name of this PowerFormRecipient.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PowerFormRecipient.

          # noqa: E501

        :param name: The name of this PowerFormRecipient.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def recipient_type(self):
        """Gets the recipient_type of this PowerFormRecipient.  # noqa: E501

          # noqa: E501

        :return: The recipient_type of this PowerFormRecipient.  # noqa: E501
        :rtype: str
        """
        return self._recipient_type

    @recipient_type.setter
    def recipient_type(self, recipient_type):
        """Sets the recipient_type of this PowerFormRecipient.

          # noqa: E501

        :param recipient_type: The recipient_type of this PowerFormRecipient.  # noqa: E501
        :type: str
        """

        self._recipient_type = recipient_type

    @property
    def role_name(self):
        """Gets the role_name of this PowerFormRecipient.  # noqa: E501

        Optional element. Specifies the role name associated with the recipient.<br/><br/>This is required when working with template recipients.  # noqa: E501

        :return: The role_name of this PowerFormRecipient.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this PowerFormRecipient.

        Optional element. Specifies the role name associated with the recipient.<br/><br/>This is required when working with template recipients.  # noqa: E501

        :param role_name: The role_name of this PowerFormRecipient.  # noqa: E501
        :type: str
        """

        self._role_name = role_name

    @property
    def routing_order(self):
        """Gets the routing_order of this PowerFormRecipient.  # noqa: E501

        Specifies the routing order of the recipient in the envelope.   # noqa: E501

        :return: The routing_order of this PowerFormRecipient.  # noqa: E501
        :rtype: str
        """
        return self._routing_order

    @routing_order.setter
    def routing_order(self, routing_order):
        """Sets the routing_order of this PowerFormRecipient.

        Specifies the routing order of the recipient in the envelope.   # noqa: E501

        :param routing_order: The routing_order of this PowerFormRecipient.  # noqa: E501
        :type: str
        """

        self._routing_order = routing_order

    @property
    def template_requires_id_lookup(self):
        """Gets the template_requires_id_lookup of this PowerFormRecipient.  # noqa: E501

          # noqa: E501

        :return: The template_requires_id_lookup of this PowerFormRecipient.  # noqa: E501
        :rtype: str
        """
        return self._template_requires_id_lookup

    @template_requires_id_lookup.setter
    def template_requires_id_lookup(self, template_requires_id_lookup):
        """Sets the template_requires_id_lookup of this PowerFormRecipient.

          # noqa: E501

        :param template_requires_id_lookup: The template_requires_id_lookup of this PowerFormRecipient.  # noqa: E501
        :type: str
        """

        self._template_requires_id_lookup = template_requires_id_lookup

    @property
    def user_name_locked(self):
        """Gets the user_name_locked of this PowerFormRecipient.  # noqa: E501

          # noqa: E501

        :return: The user_name_locked of this PowerFormRecipient.  # noqa: E501
        :rtype: str
        """
        return self._user_name_locked

    @user_name_locked.setter
    def user_name_locked(self, user_name_locked):
        """Sets the user_name_locked of this PowerFormRecipient.

          # noqa: E501

        :param user_name_locked: The user_name_locked of this PowerFormRecipient.  # noqa: E501
        :type: str
        """

        self._user_name_locked = user_name_locked

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PowerFormRecipient, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PowerFormRecipient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
