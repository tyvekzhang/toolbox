"""Kubernetes operation controller"""

from fastapi import APIRouter, Depends, WebSocket

from src.common.schema.schema import CurrentUser
from src.common.security.security import get_current_user
from src.common.util.ws import handle_playbook_result
from src.starter.factory.service_factory import (
    get_k8s_service,
)
from src.starter.schema.k8s_schema import K8sInitCmd
from src.starter.service.k8s_service import K8sService

k8s_router = APIRouter()
k8s_service: K8sService = get_k8s_service()


@k8s_router.websocket("/init")
async def init_k8s(
    websocket: WebSocket, current_user: CurrentUser = Depends(get_current_user)
):
    await websocket.accept()
    while True:
        req = await websocket.receive_text()
        k8sInitCmd: K8sInitCmd = K8sInitCmd.parse_raw(req)
        process = await k8s_service.k8s_init(k8sInitCmd)
        await handle_playbook_result(process, websocket)
