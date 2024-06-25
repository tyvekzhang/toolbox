"""K8s domain schema"""

from typing import List

from src.starter.schema.base_deploy_schema import BaseDeployCmd


class K8sInitCmd(BaseDeployCmd):
    etcd_host_ids: List[int]
    kube_master_host_ids: List[int]
    kube_worker_host_ids: List[int]
