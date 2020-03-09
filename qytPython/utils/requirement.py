"""
    module(requirement) - Python依赖.

    Main members:

        # check_requirement - 检查依赖.
"""
from qytPython import logger

# 模块与pypi对应关系
module_pypi_config = {
    'docx': 'python-docx',
    'yaml': 'PyYAML'
}


def check_requirement(module_obj, module_name):
    """ 检查依赖.

        @params:
            module_obj - 模块对象.
            module_name - 模块名.

        @return:
            On success - 检查成功返回True.
            On failure - 依赖缺少Exception信息.
    """
    logger.info('module_obj:{}'.format(module_obj))
    if module_obj is None:
        pypi_name = module_pypi_config.get(module_name, module_name)
        raise Exception('缺少依赖，您可以执行以下命令进行安装： \npip install {}'.format(pypi_name))
    return True
