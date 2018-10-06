import opc
from PIL import Image

ZO_PIXEL_COUNT = 591  # The total pixels (ie. LEDs) on the display
ZO_X_SIZE = 38  # The X dimension ie. columns
ZO_Y_SIZE = 28  # The Y dimension ie. rows


class ZeroOneException(Exception):
    """  Massively complex override of the base exception class for ZeroOne exceptions """

    def __init__(self, message, error_code=0):
        super().__init__(self)
        self.message = message
        self.error_code = error_code

    # Forget to do this and it will recurse like a motherf...er
    def __str__(self):
        return "{0} ({1})".format(self.message, self.error_code)


# TODO : Not sure we need this class any more
class ZeroOne(object):
    def __init__(self):
        pass
