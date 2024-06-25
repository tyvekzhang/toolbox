"""Goods operation mapper"""

from src.common.persistence.sqlmodel_impl import SqlModelMapper
from src.starter.model.goods_do import GoodsDO


class GoodsMapper(SqlModelMapper[GoodsDO]):
    pass


goodsMapper = GoodsMapper(GoodsDO)
