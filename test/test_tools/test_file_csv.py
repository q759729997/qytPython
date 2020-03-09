"""
    main_module - csv读写测试，测试是将对应方法的@unittest.skip注释掉.

    Main members:

        # __main__ - 程序入口.
"""
import unittest
import sys

sys.path.insert(0, './')  # 定义搜索路径的优先顺序，序号从0开始，表示最大优先级

import qytPython  # noqa
print('qytPython module path :{}'.format(qytPython.__file__))  # 输出测试模块文件位置
from qytPython.tools.file_csv import write_csv_file  # noqa
from qytPython.tools.file_csv import read_csv_file # noqa
from qytPython.tools.file_csv import read_csv_file_iter  # noqa


class TestFileCSV(unittest.TestCase):
    """ csv读写测试单元测试.

    Main methods:
        test_write_csv_file - 测试输出csv文件.
        test_read_csv_file - 测试读取csv文件内容，列表形式返回.
    """

    # @unittest.skip('debug')
    def test_write_csv_file(self):
        """ 测试递归读取输入路径下的所有文件.
        """
        print('{} test_write_csv_file {}'.format('-'*15, '-'*15))
        file_name = './data/temp.csv'
        titles = ['title', 'keyword', 'content']
        row_datas = [
            ['元旦了', '元旦', '2020年1月1日是元旦。'],
            ['天气晴朗', '晴朗，天气', '2020年1月1日是元旦，天气很不错。'],
        ]
        write_csv_file(file_name, titles, row_datas)

    @unittest.skip('debug')
    def test_read_csv_file(self):
        """ 测试读取csv文件内容，列表形式返回.
        """
        print('{} test_read_csv_file {}'.format('-'*15, '-'*15))
        file_name = './test/dataset/text.csv'
        row_datas = read_csv_file(file_name)
        print(row_datas[:3])
        # 输出：[OrderedDict([('title', '元旦了'), ('keyword', '元旦'), ('content', '2020年1月1日是元旦。')]), OrderedDict([('title', '天气晴朗'), ('keyword', '晴朗，天气'), ('content', '2020年1月1日是元旦，天气很不错。')])]

    # @unittest.skip('debug')
    def test_read_csv_file_iter(self):
        """ 测试读取csv文件内容，迭代器形式返回.
        """
        print('{} test_read_csv_file_iter {}'.format('-'*15, '-'*15))
        file_name = './test/dataset/text.csv'
        row_datas = read_csv_file_iter(file_name)
        print(row_datas)
        # 输出：<generator object read_csv_file_iter at 0x000002DCC1CDB048>
        for index, row_data in enumerate(row_datas):
            if index > 3:
                break
            print(row_data)
        # 输出：OrderedDict([('title', '元旦了'), ('keyword', '元旦'), ('content', '2020年1月1日是元旦。')])
        # OrderedDict([('title', '天气晴朗'), ('keyword', '晴朗，天气'), ('content', '2020年1月1日是元旦，天气很不错。')])


if __name__ == "__main__":
    unittest.main()  # 运行当前源文件中的所有测试用例
