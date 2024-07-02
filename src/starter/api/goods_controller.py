"""Goods operation controller"""
from typing import Dict

from fastapi import APIRouter, UploadFile, File, Depends

from src.common.result import result
from src.common.schema.schema import CurrentUser
from src.common.security.security import get_current_user
from src.starter.enum.system import SystemResponseCode
from src.starter.exception.system import SystemException
from src.starter.factory.service_factory import get_goods_service
from src.starter.model.goods_do import GoodsDO
from src.starter.service.goods_service import GoodsService

goods_router = APIRouter()
goods_service: GoodsService = get_goods_service()


@goods_router.post("/")
async def upload_zip(
    file: UploadFile = File(...),
    file_name: str = None,
    url: str = None,
    description: str = None,
    current_user: CurrentUser = Depends(get_current_user()),
):
    if not file.filename.endswith(".zip"):
        raise SystemException(
            code=SystemResponseCode.MEDIA_TYPE_ERROR.code,
            msg=SystemResponseCode.MEDIA_TYPE_ERROR.msg,
        )

    # 读取 ZIP 文件为二进制流
    binary_data = await file.read()
    goods_record = GoodsDO(
        name=file_name, pic_url=url, description=description, data=binary_data
    )
    response = await goods_service.save(record=goods_record)
    return result.success(data=response.id)


@goods_router.get("/goods")
async def get_goods(
    page: int = 1,
    size: int = 20,
    current_user: CurrentUser = Depends(get_current_user()),
) -> Dict:
    response = await goods_service.list_goods(page, size)
    return result.success(data=response)
