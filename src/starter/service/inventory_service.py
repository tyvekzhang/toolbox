"""Inventory domain service interface"""

from abc import ABC

from src.common.service.service import Service
from src.starter.model.inventory_do import InventoryDO


class InventoryService(Service[InventoryDO], ABC):
    async def ping_ip(self, *, ip_address: str, timeout: int = 4): ...
