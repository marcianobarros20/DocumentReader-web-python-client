# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from regula.documentreader.webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from regula.documentreader.webclient.gen.models import *


class GraphicFieldType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    "Document holder photo"
    PORTRAIT = int("201")

    "Fingerprint of document holder"
    FINGERPRINT = int("202")

    "Image of the iris of document holder"
    EYE = int("203")

    "Signature of document holder"
    SIGNATURE = int("204")

    "Barcode image"
    BAR_CODE = int("205")

    "Image of document confirming owner citizenship"
    PROOF_OF_CITIZENSHIP = int("206")

    "Cropped and rotated with perspective compensation (front side) of a document. Single input image can contain multiple document side/pages, which will be returned as separated results. Most coordinates in other types defined on that image."
    DOCUMENT_FRONT = int("207")

    "Image of the rear side of the document"
    DOCUMENT_REAR = int("208")

    "Area with dynamic color change"
    COLOR_DYNAMIC = int("209")

    "Additional Portrait"
    GHOST_PORTRAIT = int("210")

    "Stamp"
    STAMP = int("211")

    "Undefined image type"
    OTHER = int("250")

    "Fingerprint (thumb, left hand)"
    FINGER_LEFT_THUMB = int("300")

    "Fingerprint (index, left hand)"
    FINGER_LEFT_INDEX = int("301")

    "Fingerprint (middle, left hand)"
    FINGER_LEFT_MIDDLE = int("302")

    "Fingerprint (ring, left hand)"
    FINGER_LEFT_RING = int("303")

    "Fingerprint (little, left hand)"
    FINGER_LEFT_LITTLE = int("304")

    "Fingerprint (thumb, right hand)"
    FINGER_RIGHT_THUMB = int("305")

    "Fingerprint (index, right hand)"
    FINGER_RIGHT_INDEX = int("306")

    "Fingerprint (middle, right hand)"
    FINGER_RIGHT_MIDDLE = int("307")

    "Fingerprint (ring, right hand)"
    FINGER_RIGHT_RING = int("308")

    "Fingerprint (little, right hand)"
    FINGER_RIGHT_LITTLE = int("309")

    allowable_values = [PORTRAIT, FINGERPRINT, EYE, SIGNATURE, BAR_CODE, PROOF_OF_CITIZENSHIP, DOCUMENT_FRONT, DOCUMENT_REAR, COLOR_DYNAMIC, GHOST_PORTRAIT, STAMP, OTHER, FINGER_LEFT_THUMB, FINGER_LEFT_INDEX, FINGER_LEFT_MIDDLE, FINGER_LEFT_RING, FINGER_LEFT_LITTLE, FINGER_RIGHT_THUMB, FINGER_RIGHT_INDEX, FINGER_RIGHT_MIDDLE, FINGER_RIGHT_RING, FINGER_RIGHT_LITTLE]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """GraphicFieldType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GraphicFieldType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GraphicFieldType):
            return True

        return self.to_dict() != other.to_dict()
