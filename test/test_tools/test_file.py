"""
    main_module - 文件与文件夹处理测试，测试是将对应方法的@unittest.skip注释掉.

    Main members:

        # __main__ - 程序入口.
"""
import unittest
import sys

sys.path.insert(0, './')  # 定义搜索路径的优先顺序，序号从0开始，表示最大优先级

import qytPython  # noqa
print('qytPython module path :{}'.format(qytPython.__file__))  # 输出测试模块文件位置
from qytPython.tools.file import get_file_names_recursion  # noqa
from qytPython.tools.file import read_file_texts  # noqa
from qytPython.tools.file import read_file_iter  # noqa
from qytPython.tools.file import read_yaml_config   # noqa
from qytPython.tools.file import unzip_file  # noqa


class TestFile(unittest.TestCase):
    """ 文件与文件夹处理模块单元测试.

    Main methods:
        test_get_file_names_recursion - 测试递归读取输入路径下的所有文件.
        test_read_file_texts - 测试读取文件内容.
        test_read_file_iter - 测试读取文件内容，使用迭代器返回.
        test_read_yaml_config - 测试解析yaml配置文件.
        test_unzip_file - 测试解压zip文件.
    """
    @unittest.skip('debug')
    def test_get_file_names_recursion(self):
        """ 测试递归读取输入路径下的所有文件.
        """
        print('{} test_get_file_names_recursion {}'.format('-'*15, '-'*15))
        path = './test'
        file_names = list()
        get_file_names_recursion(path, file_names)
        print(file_names[:5])
        # 输出：['./test\\dataset\\config.yaml', './test\\dataset\\text.txt', './test\\test_tools\\test_file.py', './test\\test_tools\\test_text.py']

    @unittest.skip('debug')
    def test_read_file_texts(self):
        """ 测试读取文件内容.
        """
        print('{} test_read_file_texts {}'.format('-'*15, '-'*15))
        file_name = './test/dataset/text.txt'
        texts = read_file_texts(file_name)
        print(texts[:5])
        # 输出：['中共中央/nt 致/o 中国致公党十一大/nt 的贺词/o', '各位代表、各位同志：/o', '中国共产党中央委员会/nt', '１９９７年１１月１日/o', '（/o 新华社/nt 北京/ns １１月１日电）/o']
        texts = read_file_texts(file_name, keep_original=True)
        print(texts[:5])
        # 输出：['中共中央/nt 致/o 中国致公党十一大/nt 的贺词/o \r\n', '各位代表、各位同志：/o \r\n', '中国共产党中央委员会/nt \r\n', '１９９７年１１月１日/o \r\n', '（/o 新华社/nt 北京/ns １１月１日电）/o ']

    @unittest.skip('debug')
    def test_read_file_iter(self):
        """ 测试读取文件内容，使用迭代器返回.
        """
        print('{} test_read_file_iter {}'.format('-'*15, '-'*15))
        file_name = './test/dataset/text.txt'
        texts = read_file_iter(file_name)
        print(texts)
        # 输出：<generator object read_file_iter at 0x0000014734951780>
        texts_for_print = list()
        for index, text in enumerate(texts):
            if index > 5:
                break
            texts_for_print.append(text)
        print(texts_for_print)
        # 输出：'中共中央/nt 致/o 中国致公党十一大/nt 的贺词/o', '各位代表、各位同志：/o', '中国共产党中央委员会/nt', '１９９７年１１月１日/o', '（/o 新华社/nt 北京/ns １１月１日电）/o']
        texts = read_file_iter(file_name, keep_original=True)
        print(texts)
        # 输出：<generator object read_file_iter at 0x00000147349517D8>
        texts_for_print = list()
        for index, text in enumerate(texts):
            if index > 5:
                break
            texts_for_print.append(text)
        print(texts_for_print)
        # 输出：['中共中央/nt 致/o 中国致公党十一大/nt 的贺词/o \r\n', '各位代表、各位同志：/o \r\n', '中国共产党中央委员会/nt \r\n', '１９９７年１１月１日/o \r\n', '（/o 新华社/nt 北京/ns １１月１日电）/o ']

    # @unittest.skip('debug')
    def test_read_yaml_config(self):
        """ 测试解析yaml配置文件.
        """
        print('{} test_read_yaml_config {}'.format('-'*15, '-'*15))
        file_name = './test/dataset/config.yaml'
        config = read_yaml_config(file_name)
        print(config)
        # 输出：{'path': {'model_file': './models'}, 'params': {'thread': 5}, 'server': {'port': 12345}}

    @unittest.skip('debug')
    def test_unzip_file(self):
        """ 测试解压zip文件
        """
        print('{} test_unzip_file {}'.format('-'*15, '-'*15))
        zip_file = './test/dataset/data.zip'
        file_path = './data/zip_temp'
        unzip_file(zip_file, file_path)


if __name__ == "__main__":
    unittest.main()  # 运行当前源文件中的所有测试用例
