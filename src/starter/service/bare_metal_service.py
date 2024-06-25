"""Bare metal domain service interface"""

from abc import ABC

from src.starter.schema.bare_metal_schema import (
    RedisDeployCmd,
    UserDeployCmd,
    JreDeployCmd,
    GithubHostDeployCmd,
    NodejsDeployCmd,
    NginxDeployCmd,
    MysqlDeployCmd,
)
from src.starter.schema.base_deploy_schema import BaseDeployCmd
from src.starter.service.base_deploy_service import BaseDeployService


class BareMetalService(BaseDeployService, ABC):
    async def redis_deploy(self, redisDeployCmd: RedisDeployCmd): ...

    async def no_parm_deploy(self, baseDeployCmd: BaseDeployCmd): ...

    async def user_deploy(self, userDeployCmd: UserDeployCmd): ...

    async def jre_deploy(self, jreDeployCmd: JreDeployCmd): ...

    async def github_host_deploy(self, githubHostDeployCmd: GithubHostDeployCmd): ...

    async def nodejs_deploy(self, nodejsDeployCmd: NodejsDeployCmd): ...

    async def nginx_deploy(self, nginxDeployCmd: NginxDeployCmd): ...

    async def mysql_deploy(self, mysqlDeployCmd: MysqlDeployCmd): ...
