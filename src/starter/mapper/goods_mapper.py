"""Goods operation mapper"""

from typing import Union, Dict, List

from sqlalchemy import func
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.common.persistence.sqlmodel_impl import SqlModelMapper
from src.starter.model.goods_do import GoodsDO


class GoodsMapper(SqlModelMapper[GoodsDO]):
    async def list_goods(
            self,
            page: int,
            size: int,
            db_session: Union[AsyncSession, None] = None
    ) -> Dict[str, Union[List[Dict[str, Union[int, str]]], int]]:
        db_session = db_session or self.db.session

        # 构建基本查询
        query = select(GoodsDO.id, GoodsDO.name, GoodsDO.pic_url, GoodsDO.description)

        # 计算总数
        count_query = select(func.count()).select_from(GoodsDO)
        total_count = await db_session.scalar(count_query)

        # 分页
        paginated_query = query.offset((page - 1) * size).limit(size)

        # 执行查询
        result = await db_session.execute(paginated_query)
        records = result.fetchall()

        # 转换结果为字典列表
        goods_list = [
            {
                "id": record.id,
                "name": record.name,
                "pic_url": record.pic_url,
                "description": record.description
            }
            for record in records
        ]

        return {
            "items": goods_list,
            "total": total_count,
            "page": page,
            "size": size
        }


goodsMapper = GoodsMapper(GoodsDO)
