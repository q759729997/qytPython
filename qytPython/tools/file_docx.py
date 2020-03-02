# https://python-docx.readthedocs.io/en/latest/user/install.html
# https://www.cnblogs.com/program-in-chinese/p/10500103.html
from docx import Document
from .text import remove_blank


def read_docx_tables(file_name):
    """ 读取docx中的表格数据.

        @params:
            file_name - docx文件名.

        @return:
            On success - 表格数据列表.
            On failure - 错误信息.
    """
    file_reader = Document(file_name)
    tables = file_reader.tables
    print('tables len:{}'.format(len(tables)))
    formated_tables = list()
    # 表格数据解析
    for table in tables:
        formated_table = list()
        for row in table.rows:
            formated_row = list()
            for column in row.cells:
                text = remove_blank(column.text)
                formated_row.append(text)
            formated_table.append(formated_row)
        formated_tables.append(formated_table)
    return formated_tables
