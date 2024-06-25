"""Goods data object"""

from sqlalchemy import BLOB
from sqlmodel import Field, Column, String, SQLModel

from src.common.persistence.base_model import ModelExt, BaseModel


class BaseGoods(SQLModel):
    name: str = Field(
        sa_column=Column(
            String(64), index=True, unique=True, nullable=True, comment="名称"
        )
    )
    pic_url: str = Field(
        sa_column=Column(String(128), nullable=True, comment="封面图url")
    )
    description: str = Field(
        default=None, sa_column=Column(String(255), nullable=True, comment="描述")
    )
    data: bytes = Field(sa_column=Column(BLOB, nullable=True, comment="二进制数据"))


class GoodsDO(ModelExt, BaseGoods, BaseModel, table=True):
    __tablename__ = "sys_goods"
    __table_args__ = {"comment": "商店货物表"}
