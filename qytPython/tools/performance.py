"""
    my_module - Python性能评测.

    Main members:

        # analyze_func_run_time - 程序运行时间.
        # RunTimeBenchmark - 耗时基类.
"""
import time
from timeit import Timer

from qytPython import logger


def analyze_func_run_time(func, run_times=1):
    """ 程序运行时间.

        @params:
            func - 待评测的函数.
            run_times - 运行次数.

        @return:
            On success - 运行时间.
            On failure - 错误信息.
    """
    t1 = Timer(func)
    run_time = t1.timeit(run_times)
    logger.info("{} {:10.6} s".format(func.__name__ + ":", run_time))
    return run_time


class RunTimeBenchmark():
    """耗时基类;
    使用方式：with RunTimeBenchmark('耗时测试：'):
    """
    def __init__(self, prefix=None):
        self.prefix = prefix + ' ' if prefix else ''

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        print('%stime: %.4f sec' % (self.prefix, time.time() - self.start))