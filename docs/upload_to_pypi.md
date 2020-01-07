# 上传至pypi

- 命令

~~~python
python setup.py sdist bdist_wheel  # 打包
ls dist/  # 查看打包文件
twine upload dist/*.whl  # 将打包后的whl上传
~~~
