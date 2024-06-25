"""Inventory operation controller"""

from typing import List, Dict

from fastapi import APIRouter, Depends, Query

from src.common.result import result
from src.common.schema.schema import CurrentUser
from src.common.security.security import get_current_user
from src.starter.factory.service_factory import get_inventory_service
from src.starter.model.inventory_do import InventoryDO
from src.starter.schema.inventory_schema import InventoryCreateCmd
from src.starter.service.inventory_service import InventoryService

inventory_router = APIRouter()
inventory_service: InventoryService = get_inventory_service()


@inventory_router.post("/")
async def create_inventory(
    inventory_create_cmd: InventoryCreateCmd,
    current_user: CurrentUser = Depends(get_current_user()),
) -> Dict:
    """
    Creates a new inventory with the provided data.

    Args:

        inventory_create_cmd: Command with inventory creation data.

        current_user: Current user performing the action.
    Returns:
        BaseResponse with created inventory ID.
    """
    ipv4_address = inventory_create_cmd.ipv4_address
    ipv6_address = inventory_create_cmd.ipv6_address
    if ipv4_address:
        await inventory_service.ping_ip(ip_address=ipv4_address)
    if ipv6_address:
        await inventory_service.ping_ip(ip_address=ipv6_address)
    inventory: InventoryDO = await inventory_service.save(
        record=InventoryDO(**inventory_create_cmd.model_dump())
    )
    return result.success(data=inventory.id)


@inventory_router.get("/inventories")
async def get_inventory(
    ids: List[int] = Query(...),
    current_user: CurrentUser = Depends(get_current_user()),
) -> dict:
    """
    Retrieves inventories by a list of ID.

    Args:

        ids: The unique identifiers of the inventories.

        current_user: Current user performing the action.

    Returns:
        BaseResponse with a list of InventoryDO details.
    """
    return result.success(data=await inventory_service.retrieve_by_ids(ids=ids))
