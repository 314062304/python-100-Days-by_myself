#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 也可以按照如下所示的方式来区分到底要使用哪一个`foo`函数。

import e05_01 as m1
import e05_02 as m2

m1.foo()
m2.foo()

# 但是如果将代码写成了下面的样子，那么程序中调用的是最后导入的那个`foo`，因为后导入的foo覆盖了之前导入的`foo`。

from e05_01 import foo
from e05_02 import foo

# 输出goodbye, world!
foo()

from e05_02 import foo
from e05_01 import foo

# 输出hello, world!
foo()