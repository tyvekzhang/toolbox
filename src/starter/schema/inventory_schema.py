"""Inventory domain schema"""

import re
from typing import Optional

from pydantic import BaseModel, field_validator, model_validator


class InventoryCreateCmd(BaseModel):
    hostname: str
    password: str
    ipv4_address: Optional[str] = None
    ipv6_address: Optional[str] = None
    vault_id: Optional[str] = None
    vault: Optional[str] = None
    status: int = 1

    @field_validator("password")
    def password_must_be_strong(cls, v):
        if len(v) < 6:
            raise ValueError("password must be at least 6 characters long")
        return v

    @field_validator("ipv4_address")
    def ipv4_address_must_be_valid(cls, v):
        if v and not re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", v):
            raise ValueError("invalid IPv4 address")
        return v

    @field_validator("ipv6_address")
    def ipv6_address_must_be_valid(cls, v):
        if v and not re.match(r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$", v):
            raise ValueError("invalid IPv6 address")
        return v

    @model_validator(mode="before")
    def ipv4_or_ipv6_must_be_present(cls, values):
        ipv4 = values.get("ipv4_address")
        ipv6 = values.get("ipv6_address")
        if not ipv4 and not ipv6:
            raise ValueError("Either ipv4_address or ipv6_address must be provided")
        return values
