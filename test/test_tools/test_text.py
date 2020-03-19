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
from qytPython.tools.text import decode_bytes  # noqa


class TestText(unittest.TestCase):
    """ 文本处理模块单元测试.

    Main methods:
        test_remove_blank - 测试空白字符替换.
        test_get_json_dumps - 测试Python复杂数据类型转json字符串.
        test_decode_bytes - 字节流解码为字符串文本.
    """
    @unittest.skip('debug')
    def test_remove_blank(self):
        """ 测试空白字符替换.
        """
        print('{} test_remove_blank {}'.format('-'*15, '-'*15))
        text = '你好   哈哈 \n  哈哈哈  \t 搜索'
        print(text)
        print(remove_blank(text=text))  # 输出：你好哈哈哈哈哈搜索
        print(remove_blank(text=text, replace_text=' '))  # 输出：你好 哈哈 哈哈哈 搜索

    @unittest.skip('debug')
    def test_get_json_dumps(self):
        """ 测试Python复杂数据类型转json字符串.
        """
        print('{} test_get_json_dumps {}'.format('-'*15, '-'*15))
        json_obj = {'键1': '数值1', '键2': ['你好', '世界']}
        print(get_json_dumps(json_obj))
        # 输出：{"键1": "数值1", "键2": ["你好", "世界"]}
        print(json.dumps(json_obj))
        # 输出：{"\u952e1": "\u6570\u503c1", "\u952e2": ["\u4f60\u597d", "\u4e16\u754c"]}

    # @unittest.skip('debug')
    def test_decode_bytes(self):
        """ 字节流解码为字符串文本.
        """
        print('{} test_decode_bytes {}'.format('-'*15, '-'*15))
        byte_streams = [
            b'Hello, world!',
            '离离原上草，一岁一枯荣'.encode('gbk'),
            '离离原上草，一岁一枯荣'.encode('utf-8')
        ]
        for byte_stream in byte_streams:
            print('原始字节流:{}'.format(byte_stream))
            print('解码结果:{}'.format(decode_bytes(byte_stream=byte_stream)))
            print('解码并返回编码类型:{}'.format(decode_bytes(byte_stream=byte_stream, return_encoding_type=True)))
        """输出结果：
        始字节流:b'Hello, world!'
        解码结果:Hello, world!
        解码并返回编码类型:('Hello, world!', 'ascii')
        原始字节流:b'\xc0\xeb\xc0\xeb\xd4\xad\xc9\xcf\xb2\xdd\xa3\xac\xd2\xbb\xcb\xea\xd2\xbb\xbf\xdd\xc8\xd9'
        解码结果:离离原上草，一岁一枯荣
        解码并返回编码类型:('离离原上草，一岁一枯荣', 'GB2312')
        原始字节流:b'\xe7\xa6\xbb\xe7\xa6\xbb\xe5\x8e\x9f\xe4\xb8\x8a\xe8\x8d\x89\xef\xbc\x8c\xe4\xb8\x80\xe5\xb2\x81\xe4\xb8\x80\xe6\x9e\xaf\xe8\x8d\xa3'
        解码结果:离离原上草，一岁一枯荣
        解码并返回编码类型:('离离原上草，一岁一枯荣', 'utf-8')
        """


if __name__ == "__main__":
    unittest.main()  # 运行当前源文件中的所有测试用例
