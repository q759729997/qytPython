"""
    my_module - Python性能评测.

    Main members:

        # analyze_func_run_time - 程序运行时间.
"""
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
