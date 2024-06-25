"""Common schema"""

from pydantic import BaseModel


class Token(BaseModel):
    """
    Token schema
    """

    access_token: str
    token_type: str
    expired_at: int
    refresh_token: str
    re_expired_at: int


class CurrentUser(BaseModel):
    """
    CurrentUser schema
    """

    user_id: int


class BasePage(BaseModel):
    """
    Paging schema
    """

    page: int = 1
    size: int = 10
    count: bool = False
