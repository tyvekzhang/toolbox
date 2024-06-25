"""Base domain schema"""

from typing import List

from pydantic import BaseModel


class BaseDeployCmd(BaseModel):
    host_ids: List[int]
    goods_id: int
