#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" 屏显跑马灯  """

import os
import time

def main():
    content = '一月工资一千三，全部消费我买单!!!.....'
    # counter = 0
    while True:
        os.system('cls')  # os.system('clear')
        print(content)

        # 休眠200毫秒=0.2秒
        time.sleep(0.2)
        content = content[1:] + content[0]

        # counter += 1
        # if counter >= 50:
        #     break

if __name__ == '__main__':
    main()