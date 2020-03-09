"""
    main_module - 文本处理测试，测试是将对应方法的@unittest.skip注释掉.

    Main members:

        # __main__ - 程序入口.
"""
import json
import unittest
import sys

sys.path.insert(0, './')  # 定义搜索路径的优先顺序，序号从0开始，表示最大优先级

import qytPython  # noqa
print('qytPython module path :{}'.format(qytPython.__file__))  # 输出测试模块文件位置
from qytPython.tools.text import remove_blank  # noqa
from qytPython.tools.text import get_json_dumps  # noqa


class TestText(unittest.TestCase):
    """ 文本处理模块单元测试.

    Main methods:
        test_remove_blank - 测试空白字符替换.
        test_get_json_dumps - 测试Python复杂数据类型转json字符串.
    """
    # @unittest.skip('debug')
    def test_remove_blank(self):
        """ 测试空白字符替换.
        """
        print('{} test_remove_blank {}'.format('-'*15, '-'*15))
        text = '你好   哈哈 \n  哈哈哈  \t 搜索'
        print(text)
        print(remove_blank(text=text))  # 输出：你好哈哈哈哈哈搜索
        print(remove_blank(text=text, replace_text=' '))  # 输出：你好 哈哈 哈哈哈 搜索

    # @unittest.skip('debug')
    def test_get_json_dumps(self):
        """ 测试Python复杂数据类型转json字符串.
        """
        print('{} test_get_json_dumps {}'.format('-'*15, '-'*15))
        json_obj = {'键1': '数值1', '键2': ['你好', '世界']}
        print(get_json_dumps(json_obj))
        # 输出：{"键1": "数值1", "键2": ["你好", "世界"]}
        print(json.dumps(json_obj))
        # 输出：{"\u952e1": "\u6570\u503c1", "\u952e2": ["\u4f60\u597d", "\u4e16\u754c"]}


if __name__ == "__main__":
    unittest.main()  # 运行当前源文件中的所有测试用例
