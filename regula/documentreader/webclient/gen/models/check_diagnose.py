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


class CheckDiagnose(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    ""
    UNKNOW = int("0")

    ""
    PASS = int("1")

    ""
    INVALID_INPUT_DATA = int("2")

    ""
    INTERNAL_ERROR = int("3")

    ""
    EXCEPTION_IN_MODULE = int("4")

    ""
    UNCERTAIN_VERIFICATION = int("5")

    ""
    NECESSARY_IMAGE_NOT_FOUND = int("7")

    ""
    PHOTO_SIDES_NOT_FOUND = int("8")

    ""
    INVALID_CHECKSUM = int("10")

    ""
    SYNTAX_ERROR = int("11")

    ""
    LOGIC_ERROR = int("12")

    ""
    SOURCES_COMPARISON_ERROR = int("13")

    ""
    FIELDS_COMPARISON_LOGIC_ERROR = int("14")

    ""
    INVALID_FIELD_FORMAT = int("15")

    ""
    TRUE_LUMINESCENCE_ERROR = int("20")

    ""
    FALSE_LUMINESCENCE_ERROR = int("21")

    ""
    FIXED_PATTERN_ERROR = int("22")

    ""
    LOW_CONTRAST_IN_IR_LIGHT = int("23")

    ""
    INCORRECT_BACKGROUND_LIGHT = int("24")

    ""
    BACKGROUND_COMPARISON_ERROR = int("25")

    ""
    INCORRECT_TEXT_COLOR = int("26")

    ""
    PHOTO_FALSE_LUMINESCENCE = int("27")

    ""
    TOO_MUCH_SHIFT = int("28")

    ""
    FIBERS_NOT_FOUND = int("30")

    ""
    TOO_MANY_OBJECTS = int("31")

    ""
    SPECKS_IN_UV = int("33")

    ""
    TOO_LOW_RESOLUTION = int("34")

    ""
    INVISIBLE_ELEMENT_PRESENT = int("40")

    ""
    VISIBLE_ELEMENT_ABSENT = int("41")

    ""
    ELEMENT_SHOULD_BE_COLORED = int("42")

    ""
    ELEMENT_SHOULD_BE_GRAYSCALE = int("43")

    ""
    PHOTO_WHITE_IR_DONT_MATCH = int("44")

    ""
    UV_DULL_PAPER_MRZ = int("50")

    ""
    FALSE_LUMINESCENCE_IN_MRZ = int("51")

    ""
    UV_DULL_PAPER_PHOTO = int("52")

    ""
    UV_DULL_PAPER_BLANK = int("53")

    ""
    UV_DULL_PAPER_ERROR = int("54")

    ""
    FALSE_LUMINESCENCE_IN_BLANK = int("55")

    ""
    BAD_AREA_IN_AXIAL = int("60")

    ""
    FALSE_IP_PARAMETERS = int("65")

    ""
    FIELD_POS_CORRECTOR_HIGHLIGHT_IR = int("80")

    ""
    OVI_IR_INVISIBLE = int("90")

    ""
    OVI_INSUFFICIENT_AREA = int("91")

    ""
    OVI_COLOR_INVARIABLE = int("92")

    ""
    OVI_BAD_COLOR_FRONT = int("93")

    ""
    OVI_BAD_COLOR_SIDE = int("94")

    ""
    OVI_WIDE_COLOR_SPREAD = int("95")

    ""
    OVI_BAD_COLOR_PERCENT = int("96")

    ""
    HOLOGRAM_ELEMENT_ABSENT = int("100")

    ""
    HOLOGRAM_SIDE_TOP_IMAGES_ABSENT = int("101")

    ""
    HOLOGRAM_ELEMENT_PRESENT = int("102")

    ""
    PHOTO_PATTERN_INTERRUPTED = int("110")

    ""
    PHOTO_PATTERN_SHIFTED = int("111")

    ""
    PHOTO_PATTERN_DIFFERENT_COLORS = int("112")

    ""
    PHOTO_PATTERN_IR_VISIBLE = int("113")

    ""
    PHOTO_PATTERN_NOT_INTERSECT = int("114")

    ""
    PHOTO_SIZE_IS_WRONG = int("115")

    ""
    PHOTO_PATTERN_INVALID_COLOR = int("116")

    ""
    PHOTO_PATTERN_SHIFTED_VERT = int("117")

    ""
    PHOTO_PATTERN_PATTERN_NOT_FOUND = int("118")

    ""
    PHOTO_PATTERN_DIFFERENT_LINES_THICKNESS = int("119")

    ""
    PHOTO_IS_NOT_RECTANGLE = int("120")

    ""
    PHOTO_CORNERS_IS_WRONG = int("121")

    ""
    DOCUMENT_IS_CANCELLING = int("122")

    ""
    TEXT_COLOR_SHOULD_BE_BLUE = int("130")

    ""
    TEXT_COLOR_SHOULD_BE_GREEN = int("131")

    ""
    TEXT_COLOR_SHOULD_BE_RED = int("132")

    ""
    TEXT_SHOULD_BE_BLACK = int("133")

    ""
    BARCODE_WAS_READ_WITH_ERRORS = int("140")

    ""
    BARCODE_DATA_FORMAT_ERROR = int("141")

    ""
    BARCODE_SIZE_PARAMS_ERROR = int("142")

    ""
    NOT_ALL_BARCODESREAD = int("143")

    ""
    PORTRAIT_COMPARISON_PORTRAITS_DIFFER = int("150")

    ""
    PORTRAIT_COMPARISON_NO_SERVICE_REPLY = int("151")

    ""
    PORTRAIT_COMPARISON_SERVICE_ERROR = int("152")

    ""
    PORTRAIT_COMPARISON_NOT_ENOUGH_IMAGES = int("153")

    ""
    PORTRAIT_COMPARISON_NO_LIVE_PHOTO = int("154")

    ""
    PORTRAIT_COMPARISON_NO_SERVICE_LICENSE = int("155")

    ""
    PORTRAIT_COMPARISON_NO_PORTRAIT_DETECTED = int("156")

    ""
    LAST_DIAGNOSE_VALUE = int("157")

    allowable_values = [UNKNOW, PASS, INVALID_INPUT_DATA, INTERNAL_ERROR, EXCEPTION_IN_MODULE, UNCERTAIN_VERIFICATION, NECESSARY_IMAGE_NOT_FOUND, PHOTO_SIDES_NOT_FOUND, INVALID_CHECKSUM, SYNTAX_ERROR, LOGIC_ERROR, SOURCES_COMPARISON_ERROR, FIELDS_COMPARISON_LOGIC_ERROR, INVALID_FIELD_FORMAT, TRUE_LUMINESCENCE_ERROR, FALSE_LUMINESCENCE_ERROR, FIXED_PATTERN_ERROR, LOW_CONTRAST_IN_IR_LIGHT, INCORRECT_BACKGROUND_LIGHT, BACKGROUND_COMPARISON_ERROR, INCORRECT_TEXT_COLOR, PHOTO_FALSE_LUMINESCENCE, TOO_MUCH_SHIFT, FIBERS_NOT_FOUND, TOO_MANY_OBJECTS, SPECKS_IN_UV, TOO_LOW_RESOLUTION, INVISIBLE_ELEMENT_PRESENT, VISIBLE_ELEMENT_ABSENT, ELEMENT_SHOULD_BE_COLORED, ELEMENT_SHOULD_BE_GRAYSCALE, PHOTO_WHITE_IR_DONT_MATCH, UV_DULL_PAPER_MRZ, FALSE_LUMINESCENCE_IN_MRZ, UV_DULL_PAPER_PHOTO, UV_DULL_PAPER_BLANK, UV_DULL_PAPER_ERROR, FALSE_LUMINESCENCE_IN_BLANK, BAD_AREA_IN_AXIAL, FALSE_IP_PARAMETERS, FIELD_POS_CORRECTOR_HIGHLIGHT_IR, OVI_IR_INVISIBLE, OVI_INSUFFICIENT_AREA, OVI_COLOR_INVARIABLE, OVI_BAD_COLOR_FRONT, OVI_BAD_COLOR_SIDE, OVI_WIDE_COLOR_SPREAD, OVI_BAD_COLOR_PERCENT, HOLOGRAM_ELEMENT_ABSENT, HOLOGRAM_SIDE_TOP_IMAGES_ABSENT, HOLOGRAM_ELEMENT_PRESENT, PHOTO_PATTERN_INTERRUPTED, PHOTO_PATTERN_SHIFTED, PHOTO_PATTERN_DIFFERENT_COLORS, PHOTO_PATTERN_IR_VISIBLE, PHOTO_PATTERN_NOT_INTERSECT, PHOTO_SIZE_IS_WRONG, PHOTO_PATTERN_INVALID_COLOR, PHOTO_PATTERN_SHIFTED_VERT, PHOTO_PATTERN_PATTERN_NOT_FOUND, PHOTO_PATTERN_DIFFERENT_LINES_THICKNESS, PHOTO_IS_NOT_RECTANGLE, PHOTO_CORNERS_IS_WRONG, DOCUMENT_IS_CANCELLING, TEXT_COLOR_SHOULD_BE_BLUE, TEXT_COLOR_SHOULD_BE_GREEN, TEXT_COLOR_SHOULD_BE_RED, TEXT_SHOULD_BE_BLACK, BARCODE_WAS_READ_WITH_ERRORS, BARCODE_DATA_FORMAT_ERROR, BARCODE_SIZE_PARAMS_ERROR, NOT_ALL_BARCODESREAD, PORTRAIT_COMPARISON_PORTRAITS_DIFFER, PORTRAIT_COMPARISON_NO_SERVICE_REPLY, PORTRAIT_COMPARISON_SERVICE_ERROR, PORTRAIT_COMPARISON_NOT_ENOUGH_IMAGES, PORTRAIT_COMPARISON_NO_LIVE_PHOTO, PORTRAIT_COMPARISON_NO_SERVICE_LICENSE, PORTRAIT_COMPARISON_NO_PORTRAIT_DETECTED, LAST_DIAGNOSE_VALUE]  # noqa: E501

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
        """CheckDiagnose - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, CheckDiagnose):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CheckDiagnose):
            return True

        return self.to_dict() != other.to_dict()
