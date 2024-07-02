"""Goods domain service impl"""

from src.common.service.impl.service_impl import ServiceImpl
from src.starter.mapper.goods_mapper import GoodsMapper
from src.starter.model.goods_do import GoodsDO
from src.starter.service.goods_service import GoodsService


class GoodsServiceImpl(ServiceImpl[GoodsMapper, GoodsDO], GoodsService):
    def __init__(self, mapper: GoodsMapper):
        """
        Initialize the UserServiceImpl instance.

        Args:
            mapper (GoodsMapper): The UserMapper instance to use for database operations.
        """
        super().__init__(mapper=mapper)
        self.mapper = mapper

    async def list_goods(self, page, size):
        return await self.mapper.list_goods(page, size)
