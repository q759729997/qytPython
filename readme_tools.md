**目录(Table of contents)**

- [工具类使用说明文档](#工具类使用说明文档)

  - [文本处理](#文本处理)

    - [空白字符处理](#空白字符处理)

    - [转json字符串，保持中文不改变](#转json字符串，保持中文不改变)

  - [文件与文件夹处理](#文件与文件夹处理)

    - [递归读取输入路径下的所有文件](#递归读取输入路径下的所有文件)

    - [读取文件内容](#读取文件内容)

    - [读取文件内容，使用迭代器返回](#读取文件内容，使用迭代器返回)

    - [解析yaml配置文件](#解析yaml配置文件)

    - [zip包解压](#zip包解压)

  - [csv文件读写操作](#csv文件读写操作)

    - [输出csv文件](#输出csv文件)

    - [读取csv文件内容，列表形式返回](#读取csv文件内容，列表形式返回)

    - [读取csv文件内容，迭代器形式返回](#读取csv文件内容，迭代器形式返回)

  - [ftp上传下载](#ftp上传下载)

    - [通过FTP链接，下载文件](#通过FTP链接，下载文件)


# 工具类使用说明文档

## 文本处理

### 空白字符处理

- 函数定义.

~~~python
def remove_blank(text, replace_text=''):
    """ 匹配任意空白字符[\t\n\r\f]，替换为指定字符.

        @params:
            text - 字符串文本.
            replace_text - 需要替换的文本.

        @return:
            On success - 处理之后的文本.
    """
~~~

- 示例，`Example`:

~~~python
from qytPython.tools.text import remove_blank

text = '你好   哈哈 \n  哈哈哈  \t 搜索'
print(remove_blank(text=text))  
# 输出：你好哈哈哈哈哈搜索
print(remove_blank(text=text, replace_text=' '))  
# 输出：你好 哈哈 哈哈哈 搜索
~~~

### 转json字符串，保持中文不改变

- 函数定义，默认情况下`json.dumps`会将中文转为Unicode形式.

~~~python
def get_json_dumps(json_obj) -> str:
    """ Python复杂数据类型转json字符串，保持中文不改变.

        @params:
            json_obj - 待转换字符串的数据.

        @return:
            On success - json字符串.
    """
~~~

- 示例，`Example`:

~~~python
from qytPython.tools.text import get_json_dumps

json_obj = {'键1': '数值1', '键2': ['你好', '世界']}
print(get_json_dumps(json_obj))
# 输出：{"键1": "数值1", "键2": ["你好", "世界"]}
print(json.dumps(json_obj))  # 默认情况下的json.dumps
# 输出：{"\u952e1": "\u6570\u503c1", "\u952e2": ["\u4f60\u597d", "\u4e16\u754c"]}
~~~

## 文件与文件夹处理

### 递归读取输入路径下的所有文件

- 函数定义.

~~~python
def get_file_names_recursion(path, file_names):
    """ 递归读取输入路径下的所有文件，file_names会递归更新.

        @params:
            path - 待递归检索的文件夹路径.
            file_names - 待输出结果的文件名列表.

        @return:
            On success - 无返回值，文件输出至file_names中.
    """
~~~

- 示例，`Example`:

~~~python
from qytPython.tools.file import get_file_names_recursion

path = './test'
file_names = list()
get_file_names_recursion(path, file_names)
print(file_names[:5])
# 输出：['./test\\dataset\\config.yaml', './test\\dataset\\text.txt', './test\\test_tools\\test_file.py', './test\\test_tools\\test_text.py']
~~~

### 读取文件内容

- 函数定义.

~~~python
def read_file_texts(file_name, keep_original=False):
    """ 读取文件内容.

        @params:
            file_name - 文件路径.
            keep_original - 保持文件内容不变，默认会去掉空行以及每一行的左右空格.

        @return:
            On success - 文件内容列表，元素为每行.
    """
~~~

- 示例，`Example`:

~~~python
from qytPython.tools.file import read_file_texts

file_name = 'test/dataset/text.txt'
texts = read_file_texts(file_name)
print(texts[:5])
# 输出：['中共中央/nt 致/o 中国致公党十一大/nt 的贺词/o', '各位代表、各位同志：/o', '中国共产党中央委员会/nt', '１９９７年１１月１日/o', '（/o 新华社/nt 北京/ns １１月１日电）/o']
texts = read_file_texts(file_name, keep_original=True)
print(texts[:5])
# 输出：['中共中央/nt 致/o 中国致公党十一大/nt 的贺词/o \r\n', '各位代表、各位同志：/o \r\n', '中国共产党中央委员会/nt \r\n', '１９９７年１１月１日/o \r\n', '（/o 新华社/nt 北京/ns １１月１日电）/o ']
~~~

### 读取文件内容，使用迭代器返回

- 函数定义.

~~~python
def read_file_iter(file_name, keep_original=False):
    """ 读取文件内容，使用迭代器返回.

        @params:
            file_name - 文件路径.
            keep_original - 保持文件内容不变，默认会去掉空行以及每一行的左右空格.

        @return:
            On success - 文件内容迭代器.
    """
~~~

- 示例，`Example`:

~~~python
from qytPython.tools.file import read_file_iter

file_name = 'test/dataset/text.txt'
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
~~~

### 解析yaml配置文件

- 函数定义.

~~~python
def read_yaml_config(file_name):
    """ 解析yaml配置文件.

        @params:
            file_name - 文件路径.

        @return:
            On success - 解析后的配置对象，字典形式.
    """
~~~

- 示例，`Example`:

~~~python
from qytPython.tools.file import read_yaml_config

file_name = 'test/dataset/config.yaml'
config = read_yaml_config(file_name)
print(config)
# 输出：{'path': {'model_file': './models'}, 'params': {'thread': 5}, 'server': {'port': 12345}}
~~~

- 示例yaml配置：

~~~python
path:
    model_file: ./models
params:
    thread: 5
server:
    port: 12345
~~~

### zip包解压

- 函数定义.

~~~python
def unzip_file(zip_file, file_path):
    """ 解压zip文件.

        @params:
            zip_file - zip文件.
            file_path - 文件路径.

        @return:
            On success - 是否成功.
    """
~~~

- 示例，`Example`:

~~~python
from qytPython.tools.file import unzip_file

zip_file = './test/dataset/data.zip'
file_path = './data/zip_temp'
unzip_file(zip_file, file_path)
~~~

## csv文件读写操作

### 输出csv文件

- 函数定义.

~~~python
def write_csv_file(file_name, titles, row_datas):
    """ 输出csv文件，需保证title与行的内容个数一致.

        @params:
            file_name - 文件名称.
            titles - 标题列表.
            row_datas - 每一行的数据，每个元素也是一个列表或者元组.
    """
~~~

- 示例，`Example`:

~~~python
from qytPython.tools.file_csv import write_csv_file

file_name = './data/temp.csv'
titles = ['title', 'keyword', 'content']
row_datas = [
    ['元旦了', '元旦', '2020年1月1日是元旦。'],
    ['天气晴朗', '晴朗，天气', '2020年1月1日是元旦，天气很不错。'],
]
write_csv_file(file_name, titles, row_datas)
~~~

- 输出的csv文件示例：

~~~python
title,keyword,content
元旦了,元旦,2020年1月1日是元旦。
天气晴朗,晴朗，天气,2020年1月1日是元旦，天气很不错。
~~~

### 读取csv文件内容，列表形式返回

- 函数定义.

~~~python
def read_csv_file(file_name):
    """ 读取csv文件内容，列表形式返回.

        @params:
            file_name - 文件名.

        @return:
            On success - 返回每行数据的列表，列表元素为每行数据的字典形式.
    """
~~~

- 示例，`Example`:

~~~python
from qytPython.tools.file_csv import read_csv_file

file_name = './test/dataset/text.csv'
row_datas = read_csv_file(file_name)
print(row_datas[:3])
# 输出：[OrderedDict([('title', '元旦了'), ('keyword', '元旦'), ('content', '2020年1月1日是元旦。')]), OrderedDict([('title', '天气晴朗'), ('keyword', '晴朗，天气'), ('content', '2020年1月1日是元旦，天气很不错。')])]
~~~

### 读取csv文件内容，迭代器形式返回

- 函数定义.

~~~python
def read_csv_file_iter(file_name):
    """ 读取csv文件内容，迭代器形式返回.

        @params:
            file_name - 文件名.

        @return:
            On success - 返回每行数据的迭代器，迭代器元素为每行数据的字典形式.
    """
~~~

- 示例，`Example`:

~~~python
from qytPython.tools.file_csv import read_csv_file_iter

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
~~~

## ftp上传下载

### 通过FTP链接，下载文件

- 函数定义.

~~~python
def download_file(ftp_url, file_name, file_path=''):
    """ 通过FTP链接，下载文件.

        @params:
            ftp_url - ftp链接.
            file_name - 文件名.
            file_path - 文件路径.

        @return:
            On success - 是否成功.
    """
~~~

- 示例，`Example`:

~~~python
from qytPython.tools.ftp import download_file

ftp_url = 'http://39.104.161.233:80/tianchi/7000.csv'
file_name = '7000.csv'
file_path = 'data/yuchuan/'
download_file(ftp_url, file_name, file_path)
~~~
