"""Goods domain service interface"""

from abc import ABC

from src.common.service.service import Service
from src.starter.model.goods_do import GoodsDO


class GoodsService(Service[GoodsDO], ABC):
    async def list_goods(self, page, size): ...
