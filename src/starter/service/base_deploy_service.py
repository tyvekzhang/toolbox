"""Base deploy domain service interface"""

from abc import ABC

from src.starter.schema.base_deploy_schema import BaseDeployCmd


class BaseDeployService(ABC):
    async def base_deploy(self, baseDeployCmd: BaseDeployCmd): ...
