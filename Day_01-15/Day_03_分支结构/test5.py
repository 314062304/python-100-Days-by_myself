#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" 输入月收入和五险一金计算个人所得税 """

salary = float(input('本月收入： '))
insurance = float(input('五险一金: '))
diff = salary - insurance - 3500
if diff <= 0:
    rate = 0
    deduction = 0
elif 0 < diff < 1500:
    rate = 0.03
    deduction = 0
elif 1500 <= diff < 4500:
    rate = 0.1
    deduction = 105
elif 4500 <= diff < 9000:
    rate = 0.2
    deduction = 555
elif 9000 <= diff < 35000:
    rate = 0.25
    deduction = 1005
elif 35000 <= diff < 55000:
    rate = 0.3
    deduction = 2755
elif 55000 <= diff < 80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0/45
    deduction = 13505

tax = abs(diff * rate - deduction)
print('个人所得税: ￥%.2f' % tax)
print('实际到手收入: ￥%.2f' % (diff + 3500 - tax))