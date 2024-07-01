<div  align="center" style="margin-top: 3%">
   <h1>
     Toolbox
   </h1>
   <h3>
    Toolbox是最好的devops工具助手之一。
   </h3>
</div>


## 特性

- ⚡ 开箱即用, 完全实现中间件零依赖
   - 默认使用Sqlite, 也可自由切换PostgreSQL、MySQL
   - 默认使用文件缓存, 支持切换为Redis
- 🚢 支持裸机安装和云原生的方式安装常用软件
- 🚀 通过扩展ansible的自动化功能, 大大提高软件部署效率


## 文档

## 设置一个虚拟环境
> 这部分是可选的，但可能对新学 Python 的用户有用。[虚拟环境设置](https://github.com/tyvekzhang/toolbox/blob/main/docs/VIRTUAL_ENV.md)

## 快速开始
1. 克隆代码
```shell
git clone https://github.com/tyvekzhang/toolbox
cd toolbox
```
2. 安装 Poetry并下载依赖
- 通过conda虚拟环境安装, 如果安装了conda的话
  ```shell
  conda install poetry -y
  poetry install
  ```
- 或者通过pip安装
  ```shell
  pip install poetry -i https://mirrors.aliyun.com/pypi/simple/
  poetry install
  ```
3. 数据库迁移
```shell
cd src && alembic upgrade head
```
4. 启动
```shell
python apiserver.py
```
5. 交互式文档地址: http://127.0.0.1:9010/docs
6. 恭喜你, 运行成功. 接口访问前需创建用户, 并进行认证
7. 可以随时按CTRL+C停止运行

## 许可证

Toolbox 采用 [GPLv3 许可证](https://opensource.org/license/gpl-3-0)开源。
