"""
    main_module - docx读写测试，测试是将对应方法的@unittest.skip注释掉.

    Main members:

        # __main__ - 程序入口.
"""
import unittest
import sys
import pprint

sys.path.append('./')

from qytPython.tools.file_docx import read_docx_tables  # noqa
# from qytPython.tools.file_csv import write_csv_file  # noqa


class TestFileDocx(unittest.TestCase):
    """ docx读写测试单元测试.

    Main methods:
        test_read_docx_tables - 读取docx中的tables.
    """

    # @unittest.skip('debug')
    def test_read_docx_tables(self):
        """ 读取docx中的tables.
        """
        print('{} test_read_docx_tables {}'.format('-'*15, '-'*15))
        file_name = './data/tables.docx'
        # out_out_file = './data/docx_tables/table_{}.csv'
        tables = read_docx_tables(file_name)
        # # 输出：<generator object read_csv_file_iter at 0x000002DCC1CDB048>
        for index, table in enumerate(tables):
            # if index != 0:
            #     continue
            print('{} table no :{} {}'.format('-'*15, index, '-'*15))
            pprint.pprint(table)
            # csv_file_name = out_out_file.format(index + 1)
            # write_csv_file(file_name=csv_file_name, titles=None, row_datas=table)


if __name__ == "__main__":
    unittest.main()  # 运行当前源文件中的所有测试用例
