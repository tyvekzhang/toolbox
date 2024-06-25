import io
import os
import tempfile
import zipfile
from typing import Tuple, List


def generate_playbook_paths(
    zip_file_object: io.BytesIO,
) -> Tuple[tempfile.TemporaryDirectory, str, str, str, List[str]]:
    site_file = "site.yml"
    inventory_file = "inventory.ini"
    global_var_file = "global.yml"
    roles_dir_name = "roles"

    _temp_dir = tempfile.TemporaryDirectory()
    temp_dir = _temp_dir.name
    print(temp_dir)
    with zipfile.ZipFile(zip_file_object, "r") as zip_ref:
        zip_ref.extractall(temp_dir)
    zip_dir_name = os.listdir(temp_dir)[0]
    playbook_dir = os.path.join(temp_dir, zip_dir_name)
    role_names = os.listdir(os.path.join(playbook_dir, roles_dir_name))
    site_file_path = os.path.join(playbook_dir, site_file)
    inventory_file_path = os.path.join(playbook_dir, inventory_file)
    global_var_file_path = os.path.join(playbook_dir, global_var_file)

    return (
        _temp_dir,
        inventory_file_path,
        site_file_path,
        global_var_file_path,
        role_names,
    )
