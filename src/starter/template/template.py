import os.path

import jinja2
from starlette.templating import Jinja2Templates


def get_bare_metal_template(goods_name: str, template_name: str) -> jinja2.Template:
    real_path = os.path.dirname(os.path.realpath(__file__))
    bare_metal_path = os.path.join(real_path, "bare_metal")
    directory = os.path.join(bare_metal_path, goods_name)
    templates = Jinja2Templates(directory=directory)
    return templates.get_template(template_name)


def get_k8s_template(template_name: str) -> jinja2.Template:
    real_path = os.path.dirname(os.path.realpath(__file__))
    directory = os.path.join(real_path, "k8s")
    templates = Jinja2Templates(directory=directory)
    return templates.get_template(template_name)
