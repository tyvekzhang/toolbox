"""System response code"""

from enum import Enum


class SystemResponseCode(Enum):
    """
    Enum for system response codes.
    """

    def __init__(self, code, msg):
        """
        Initialize a system response code.

        Args:
            code (int): The response code.
            msg (str): The response message.
        """
        self.code = code
        self.msg = msg

    SUCCESS = (0, "Success")
    SERVICE_INTERNAL_ERROR = (-1, "Service internal error")
    PARAMETER_ERROR = (400, "Parameter error")
    AUTH_FAILED = (401, "Username or password error")
    PARAMETER_CHECK_ERROR = (402, "Parameter check error")
    MEDIA_TYPE_ERROR = (403, "media type error")
    USER_NAME_EXISTS = (100, "Username already exists")
    ROLE_ALREADY_EXISTS = (101, "Assign role already exists")


class SystemConstantCode(Enum):
    """
    Enum for system constant codes.
    """

    def __init__(self, code, msg):
        """
        Initialize a system constant code.

        Args:
            code (int): The constant code.
            msg (str): The constant message.
        """
        self.code = code
        self.msg = msg

    USER_KEY = (10, "user:")
