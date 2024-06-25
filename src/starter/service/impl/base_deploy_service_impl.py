"""Base deploy domain service impl"""

import io
import tempfile
from typing import List, Tuple

from src.common.util.file import generate_playbook_paths
from src.starter.factory.session_factory import db_session
from src.starter.mapper.goods_mapper import goodsMapper
from src.starter.mapper.inventory_mapper import inventoryMapper
from src.starter.model.goods_do import GoodsDO
from src.starter.schema.base_deploy_schema import BaseDeployCmd
from src.starter.service.base_deploy_service import BaseDeployService
from src.starter.template.template import get_bare_metal_template


class BaseDeployServiceImpl(BaseDeployService):
    def __init__(self):
        self.common_template_dir = "common"
        self.common_inventory_name = "inventory.yml"
        self.common_site_name = "site.yml"
        self.common_global_name = "global.yml"

    async def base_deploy(
        self, baseDeployCmd: BaseDeployCmd
    ) -> Tuple[tempfile.TemporaryDirectory, str, str, str, List[str]]:
        global temp_dir
        async with db_session() as session:
            goods_record: GoodsDO = await goodsMapper.select_record_by_id(
                id=baseDeployCmd.goods_id, db_session=session
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
        role_name = role_names[0]
        async with db_session() as session:
            inventory_records = await inventoryMapper.select_records_by_ids(
                ids=baseDeployCmd.host_ids, db_session=session
            )
        inventory_template = get_bare_metal_template(
            self.common_template_dir, self.common_inventory_name
        )
        site_template = get_bare_metal_template(
            self.common_template_dir, self.common_site_name
        )
        inventory_content = inventory_template.render(hosts=inventory_records)
        with open(inventory_file_path, "w", encoding="utf-8") as file:
            file.write(inventory_content)
        site_content = site_template.render(role_name=role_name)
        with open(site_file_path, "w", encoding="utf-8") as file:
            file.write(site_content)
        return (
            temp_dir,
            inventory_file_path,
            site_file_path,
            global_var_file_path,
            role_name,
        )
