"""Inventory data object"""

from typing import Optional

from sqlalchemy import SmallInteger, Integer
from sqlmodel import Field, Column, String, SQLModel

from src.common.persistence.base_model import ModelExt, BaseModel


class BaseInventory(SQLModel):
    hostname: str = Field(
        sa_column=Column(
            String(32), index=True, unique=True, nullable=True, comment="主机名"
        )
    )
    user: str = Field(
        default=None, sa_column=Column(String(32), nullable=True, comment="用户名")
    )
    password: str = Field(
        default=None, sa_column=Column(String(64), nullable=True, comment="密码")
    )
    become_user: str = Field(
        default=None, sa_column=Column(String(32), nullable=True, comment="提权用户")
    )
    become_password: str = Field(
        default=None, sa_column=Column(String(64), nullable=True, comment="提权密码")
    )
    ipv4_address: Optional[str] = Field(
        default=None, sa_column=Column(String(16), nullable=True, comment="ipv4地址")
    )
    ipv6_address: Optional[str] = Field(
        default=None, sa_column=Column(String(64), nullable=True, comment="ipv6地址")
    )
    port: Optional[int] = Field(
        default=22, sa_column=Column(Integer(), nullable=True, comment="ssh端口")
    )
    vault_id: str = Field(
        default=None, sa_column=Column(String(32), nullable=True, comment="vault标识")
    )
    vault: str = Field(
        default=None, sa_column=Column(String(32), nullable=True, comment="保险库密码")
    )
    status: int = Field(
        default=None, sa_column=Column(SmallInteger(), nullable=True, comment="状态")
    )


class InventoryDO(ModelExt, BaseInventory, BaseModel, table=True):
    __tablename__ = "sys_inventory"
    __table_args__ = {"comment": "主机清单表"}
