#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""  返回后缀名  """

def get_suffix(filename, has_dot=False):        # filename: 文件名; has_dot: 返回的后缀名是否需要带点
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''