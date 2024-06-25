"""Inventory operation mapper"""

from src.common.persistence.sqlmodel_impl import SqlModelMapper
from src.starter.model.inventory_do import InventoryDO


class InventoryMapper(SqlModelMapper[InventoryDO]):
    pass


inventoryMapper = InventoryMapper(InventoryDO)
