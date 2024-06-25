"""K8s domain service impl"""

import io
import subprocess
from typing import List

from loguru import logger

from src.common.config import configs
from src.common.enum.enum import ModeEnum
from src.common.util.file import generate_playbook_paths
from src.starter.factory.session_factory import db_session
from src.starter.mapper.goods_mapper import goodsMapper
from src.starter.mapper.inventory_mapper import inventoryMapper
from src.starter.model.goods_do import GoodsDO
from src.starter.model.inventory_do import InventoryDO
from src.starter.schema.k8s_schema import K8sInitCmd
from src.starter.service.impl.base_deploy_service_impl import (
    BaseDeployServiceImpl,
)
from src.starter.service.k8s_service import K8sService
from src.starter.template.template import get_k8s_template


class K8sServiceImpl(K8sService, BaseDeployServiceImpl):
    def __init__(self):
        super().__init__()

    async def k8s_init(self, k8sInitCmd: K8sInitCmd):
        global temp_dir
        try:
            async with db_session() as session:
                goods_record: GoodsDO = await goodsMapper.select_record_by_id(
                    id=k8sInitCmd.goods_id, db_session=session
                )
            binary_data = goods_record.data
            zip_file_object = io.BytesIO(binary_data)
            (
                temp_dir,
                inventory_file_path,
                site_file_path,
                global_var_file_path,
                role_names,
            ) = generate_playbook_paths(zip_file_object)
            async with db_session() as session:
                inventory_records: List[
                    InventoryDO
                ] = await inventoryMapper.select_records_by_ids(
                    ids=k8sInitCmd.host_ids, db_session=session
                )
            etcd_records = []
            kube_master_records = []
            kube_worker_records = []
            etcd_host_ids = set(k8sInitCmd.etcd_host_ids)
            kube_master_host_ids = set(k8sInitCmd.kube_master_host_ids)
            kube_worker_host_ids = set(k8sInitCmd.kube_worker_host_ids)
            for inventory_record in inventory_records:
                inventory_id = inventory_record.id
                if etcd_host_ids.__contains__(inventory_id):
                    etcd_records.append(inventory_record)
                if kube_master_host_ids.__contains__(inventory_id):
                    kube_master_records.append(inventory_record)
                if kube_worker_host_ids.__contains__(inventory_id):
                    kube_worker_records.append(inventory_record)
            # 覆盖默认渲染的inventory清单
            inventory_template = get_k8s_template(self.common_inventory_name)
            inventory_content = inventory_template.render(
                hosts=inventory_records,
                etcd_hosts=etcd_records,
                kube_master_hosts=kube_master_records,
                kube_worker_hosts=kube_worker_records,
            )
            with open(inventory_file_path, "w", encoding="utf-8") as file:
                file.write(inventory_content)
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
