"""
    main_module - Python性能评测，测试是将对应方法的@unittest.skip注释掉.

    Main members:

        # __main__ - 程序入口.
"""
import unittest
import sys
import time

sys.path.insert(0, './')  # 定义搜索路径的优先顺序，序号从0开始，表示最大优先级

import qytPython  # noqa
print('qytPython module path :{}'.format(qytPython.__file__))  # 输出测试模块文件位置
from qytPython.tools.performance import analyze_func_run_time  # noqa


class TestPerformance(unittest.TestCase):
    """ Python性能评测.

    Main methods:
        test_analyze_func_run_time - 程序运行时间.
    """

    # @unittest.skip('debug')
    def test_analyze_func_run_time(self):
        """ 程序运行时间.
        """
        print('{} test_analyze_func_run_time {}'.format('-'*15, '-'*15))

        def run_time_test():
            for i in range(10):
                time.sleep(0.1)

        print(analyze_func_run_time(run_time_test))  # run_time_test: 1.0073572258482262 s
        print(analyze_func_run_time(run_time_test, run_times=2))  # run_time_test: 2.0132420583797828 s


if __name__ == "__main__":
    unittest.main()  # 运行当前源文件中的所有测试用例
