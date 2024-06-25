"""BareMetal domain service impl"""

import subprocess

from loguru import logger

from src.common.config import configs
from src.common.enum.enum import ModeEnum
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
from src.starter.service.bare_metal_service import BareMetalService
from src.starter.service.impl.base_deploy_service_impl import (
    BaseDeployServiceImpl,
)
from src.starter.template.template import get_bare_metal_template


class BareMetalServiceImpl(BareMetalService, BaseDeployServiceImpl):
    def __init__(self):
        super().__init__()

    async def redis_deploy(self, redisDeployCmd: RedisDeployCmd):
        global temp_dir
        try:
            baseDeployCmd = BaseDeployCmd(
                host_ids=redisDeployCmd.host_ids, goods_id=redisDeployCmd.goods_id
            )
            (
                temp_dir,
                inventory_file_path,
                site_file_path,
                global_var_file_path,
                role_name,
            ) = await self.base_deploy(baseDeployCmd)
            global_template = get_bare_metal_template(
                role_name, self.common_global_name
            )
            global_content = global_template.render(
                redis_version=redisDeployCmd.version,
                redis_password=redisDeployCmd.password,
            )
            with open(global_var_file_path, "w", encoding="utf-8") as file:
                file.write(global_content)
            command = [
                "ansible-playbook",
                "-i",
                inventory_file_path,
                "-e",
                f"@{global_var_file_path}",
                site_file_path,
            ]
            logger.info(" ".join(command))
            return subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        finally:
            if configs.mode == ModeEnum.production:
                temp_dir.cleanup()

    async def no_parm_deploy(self, baseDeployCmd: BaseDeployCmd):
        global temp_dir
        try:
            (
                temp_dir,
                inventory_file_path,
                site_file_path,
                global_var_file_path,
                role_name,
            ) = await self.base_deploy(baseDeployCmd)
            command = [
                "ansible-playbook",
                "-i",
                inventory_file_path,
                site_file_path,
            ]
            logger.info(" ".join(command))
            return subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        finally:
            if configs.mode == ModeEnum.production:
                temp_dir.cleanup()

    async def user_deploy(self, userDeployCmd: UserDeployCmd):
        global temp_dir
        try:
            baseDeployCmd = BaseDeployCmd(
                host_ids=userDeployCmd.host_ids, goods_id=userDeployCmd.goods_id
            )
            (
                temp_dir,
                inventory_file_path,
                site_file_path,
                global_var_file_path,
                role_name,
            ) = await self.base_deploy(baseDeployCmd)
            global_template = get_bare_metal_template(
                role_name, self.common_global_name
            )
            global_content = global_template.render(
                user=userDeployCmd.user,
                password=userDeployCmd.password,
                group=userDeployCmd.group,
            )
            with open(global_var_file_path, "w", encoding="utf-8") as file:
                file.write(global_content)
            command = [
                "ansible-playbook",
                "-i",
                inventory_file_path,
                "-e",
                f"@{global_var_file_path}",
                site_file_path,
            ]
            logger.info(" ".join(command))
            return subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        finally:
            if configs.mode == ModeEnum.production:
                temp_dir.cleanup()

    async def jre_deploy(self, jreDeployCmd: JreDeployCmd):
        global temp_dir
        try:
            baseDeployCmd = BaseDeployCmd(
                host_ids=jreDeployCmd.host_ids, goods_id=jreDeployCmd.goods_id
            )
            (
                temp_dir,
                inventory_file_path,
                site_file_path,
                global_var_file_path,
                role_name,
            ) = await self.base_deploy(baseDeployCmd)
            global_template = get_bare_metal_template(
                role_name, self.common_global_name
            )
            global_content = global_template.render(version=jreDeployCmd.version)
            with open(global_var_file_path, "w", encoding="utf-8") as file:
                file.write(global_content)
            command = [
                "ansible-playbook",
                "-i",
                inventory_file_path,
                "-e",
                f"@{global_var_file_path}",
                site_file_path,
            ]
            logger.info(" ".join(command))
            return subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        finally:
            if configs.mode == ModeEnum.production:
                temp_dir.cleanup()

    async def github_host_deploy(self, githubHostDeployCmd: GithubHostDeployCmd):
        global temp_dir
        try:
            baseDeployCmd = BaseDeployCmd(
                host_ids=githubHostDeployCmd.host_ids,
                goods_id=githubHostDeployCmd.goods_id,
            )
            (
                temp_dir,
                inventory_file_path,
                site_file_path,
                global_var_file_path,
                role_name,
            ) = await self.base_deploy(baseDeployCmd)
            global_template = get_bare_metal_template(
                role_name, self.common_global_name
            )
            global_content = global_template.render(
                host=githubHostDeployCmd.host,
                host_backup=githubHostDeployCmd.host_backup,
            )
            with open(global_var_file_path, "w", encoding="utf-8") as file:
                file.write(global_content)
            command = [
                "ansible-playbook",
                "-i",
                inventory_file_path,
                "-e",
                f"@{global_var_file_path}",
                site_file_path,
            ]
            logger.info(" ".join(command))
            return subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        finally:
            if configs.mode == ModeEnum.production:
                temp_dir.cleanup()

    async def nodejs_deploy(self, nodejsDeployCmd: NodejsDeployCmd):
        global temp_dir
        try:
            baseDeployCmd = BaseDeployCmd(
                host_ids=nodejsDeployCmd.host_ids, goods_id=nodejsDeployCmd.goods_id
            )
            (
                temp_dir,
                inventory_file_path,
                site_file_path,
                global_var_file_path,
                role_name,
            ) = await self.base_deploy(baseDeployCmd)
            global_template = get_bare_metal_template(
                role_name, self.common_global_name
            )
            global_content = global_template.render(
                node_version=nodejsDeployCmd.node_version,
                nvm_version=nodejsDeployCmd.nvm_version,
            )
            with open(global_var_file_path, "w", encoding="utf-8") as file:
                file.write(global_content)
            command = [
                "ansible-playbook",
                "-i",
                inventory_file_path,
                "-e",
                f"@{global_var_file_path}",
                site_file_path,
            ]
            logger.info(" ".join(command))
            return subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        finally:
            if configs.mode == ModeEnum.production:
                temp_dir.cleanup()

    async def nginx_deploy(self, nginxDeployCmd: NginxDeployCmd):
        global temp_dir
        try:
            (
                temp_dir,
                inventory_file_path,
                site_file_path,
                global_var_file_path,
                role_name,
            ) = await self.base_deploy(nginxDeployCmd)
            command = [
                "ansible-playbook",
                "-i",
                inventory_file_path,
                site_file_path,
            ]
            logger.info(" ".join(command))
            return subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        finally:
            if configs.mode == ModeEnum.production:
                temp_dir.cleanup()

    async def mysql_deploy(self, mysqlDeployCmd: MysqlDeployCmd):
        global temp_dir
        try:
            baseDeployCmd = BaseDeployCmd(
                host_ids=mysqlDeployCmd.host_ids, goods_id=mysqlDeployCmd.goods_id
            )
            (
                temp_dir,
                inventory_file_path,
                site_file_path,
                global_var_file_path,
                role_name,
            ) = await self.base_deploy(baseDeployCmd)
            global_template = get_bare_metal_template(
                role_name, self.common_global_name
            )
            global_content = global_template.render(
                mysql_root_password=mysqlDeployCmd.mysql_root_password,
                admin=mysqlDeployCmd.admin,
                admin_password=mysqlDeployCmd.admin_password,
            )
            with open(global_var_file_path, "w", encoding="utf-8") as file:
                file.write(global_content)
            command = [
                "ansible-playbook",
                "-i",
                inventory_file_path,
                "-e",
                f"@{global_var_file_path}",
                site_file_path,
            ]
            logger.info(" ".join(command))
            return subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        finally:
            if configs.mode == ModeEnum.production:
                temp_dir.cleanup()
