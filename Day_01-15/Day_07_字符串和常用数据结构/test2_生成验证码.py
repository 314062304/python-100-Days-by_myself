#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""  生成验证码  """

import random

def generate_code(code_len=4):      # 验证码的长度(默认4个字符)
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code         # 由大小写英文字母和数字构成的随机验证码

if __name__ == '__main__':
    generate_code()
