# !/usr/bin/env python3.8
# encoding: utf-8
# Time:2023/8/6 17:29
# Author:xiaobin
# File:tools.py
# Software:PyCharm

import sys


def get_opts(name):
    """
    返回参数name的值
    :param name:
    :return:
    """
    args = sys.argv[1:]
    if name in args:
        return args[args.index(name)+1]
    else:
        return ''