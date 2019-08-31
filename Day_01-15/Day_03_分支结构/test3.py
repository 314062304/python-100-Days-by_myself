#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" 百分制成绩转等级制
90分以上       --> A
80分~89分      --> B
70分~79分      --> C
60分~69分      --> D
60分以下       --> E
"""

score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif 80 <= score <= 89:
    grade = 'B'
elif 70 <= score <= 79:
    grade = 'C'
elif 60 <= score <= 69:
    grade = 'D'
else:
    grade = 'E'

print(grade)