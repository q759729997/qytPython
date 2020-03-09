"""
    main_module - ftp上传下载测试，测试是将对应方法的@unittest.skip注释掉.

    Main members:

        # __main__ - 程序入口.
"""
import unittest
import sys

sys.path.insert(0, './')  # 定义搜索路径的优先顺序，序号从0开始，表示最大优先级

import qytPython  # noqa
print('qytPython module path :{}'.format(qytPython.__file__))  # 输出测试模块文件位置
from qytPython.tools.ftp import download_file  # noqa


class TestFile(unittest.TestCase):
    """ ftp上传下载测试.

    Main methods:
        test_download_file - 测试FTP下载.
    """
    # @unittest.skip('debug')
    def test_download_file(self):
        """ 测试FTP下载.
        """
        print('{} test_download_file {}'.format('-'*15, '-'*15))
        ftp_url = 'http://39.104.161.233:80/tianchi/7000.csv'
        file_name = '7000.csv'
        file_path = 'data/yuchuan/'
        download_file(ftp_url, file_name, file_path)


if __name__ == "__main__":
    unittest.main()  # 运行当前源文件中的所有测试用例
