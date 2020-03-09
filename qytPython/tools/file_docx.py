"""
    my_module - word操作.

    Main members:

        # read_docx_tables - 读取docx中的表格数据.

    参考资料:

        # https://python-docx.readthedocs.io/en/latest/user/install.html
        # https://www.cnblogs.com/program-in-chinese/p/10500103.html
"""
from qytPython.utils.requirement import check_requirement
# 需要判断依赖的包
try:
    import docx
except Exception:
    docx = None


def _check_requirement_docx():
    return check_requirement(docx, 'docx')


def read_docx_tables(file_name, is_formated=True):
    """ 读取docx中的表格数据.

        @params:
            file_name - docx文件名.
            is_formated - 表格数据是否格式化为普通列表，若不格式化则为docx对象形式.

        @return:
            On success - 表格数据列表.
            On failure - 错误信息.
    """
    _check_requirement_docx()
    file_reader = docx.Document(file_name)
    tables = file_reader.tables
    print('tables len:{}'.format(len(tables)))
    if not is_formated:
        return tables
    formated_tables = list()
    # 表格数据解析
    tables_len = len(tables)
    for table_id, table in enumerate(tables):
        print('process table {}/{}'.format(table_id + 1, tables_len))
        formated_table = list()
        for row in table.rows:
            formated_row = list()
            for column in row.cells:
                text = column.text
                formated_row.append(text)
            formated_table.append(formated_row)
        formated_tables.append(formated_table)
    return formated_tables
