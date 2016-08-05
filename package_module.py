#coding=utf-8
# import package_module_demo.b.test
# package_module_demo.b.test.test()

from package_module_demo.b.test import test
test()  #this is b.test(),the code is 100
from package_module_demo.a.test import test
test()  #this is a.test(),the code is 333
test(); #在这里已经将b.test()覆盖 输出 #this is a.test(),the code is 333

from package_module_demo.b.test import test as testb
testb()  #this is b.test(),the code is 100

from package_module_demo.a.test import test as testa
testa()  #this is a.test(),the code is 333

testb()  #this is b.test(),the code is 100

#在这里我们将两个子包中定义了两个一样的函数，在引用时会出现覆盖的现象 这里有两种解决方法
#第一种 直接import 然后 一层一层的往下写
# import package_module_demo.b.test
# package_module_demo.b.test.test()

#第二种 使用 as 关键字
# form package_module_demo.b.test import test as testb



