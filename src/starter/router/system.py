"""Routing of system modules"""

from fastapi import APIRouter

from src.common.config import configs
from src.starter.server import app
from src.starter.api.probe_controller import probe_router
from src.starter.api.user_controller import user_router
from src.starter.api.inventory_controller import inventory_router
from src.starter.api.goods_controller import goods_router
from src.starter.api.bare_metal_controller import bare_metal_router
from src.starter.api.k8s_controller import k8s_router

system_router = APIRouter()
system_router.include_router(probe_router, tags=["probe"], prefix="/probe")
system_router.include_router(user_router, tags=["user"], prefix="/user")
system_router.include_router(inventory_router, tags=["inventory"], prefix="/inventory")
system_router.include_router(goods_router, tags=["goods"], prefix="/goods")
system_router.include_router(k8s_router, tags=["k8s"], prefix="/k8s")
system_router.include_router(
    bare_metal_router, tags=["bare_metal"], prefix="/bare_metal"
)

# Add system routing
app.include_router(system_router, prefix=configs.api_version)
