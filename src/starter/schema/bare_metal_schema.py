"""Bare metal domain schema"""

from src.starter.schema.base_deploy_schema import BaseDeployCmd


class RedisDeployCmd(BaseDeployCmd):
    version: str
    password: str


class UserDeployCmd(BaseDeployCmd):
    user: str
    password: str
    group: str


class JreDeployCmd(BaseDeployCmd):
    version: str


class GithubHostDeployCmd(BaseDeployCmd):
    host: str = "151.101.100.133"
    host_backup: str = "185.199.111.133"


class NodejsDeployCmd(BaseDeployCmd):
    nvm_version: str = "0.39.7"
    node_version: str = "20.15.0"


class NginxDeployCmd(BaseDeployCmd):
    pass


class MysqlDeployCmd(BaseDeployCmd):
    mysql_root_password: str = "qwert!"
    admin: str = "admin"
    admin_password: str = "qwert!"
