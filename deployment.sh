#!/bin/bash
# 指定脚本版本,然后进行部署.

rm -rf ./dist/*

# 以下所有生成文件将在当前路径下 dist 目录中
python3 setup.py bdist_egg # 生成easy_install支持的格式
python3 setup.py sdist     # 生成pip支持的格式，下文以此为例
python setup.py sdist upload