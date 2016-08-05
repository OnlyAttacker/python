#coding=utf-8
from test import code
# test.code = 100 #这里没有import test 居然可以使用test模块，从而改变test.code的值
code = 222      #由于import变量做的是值传递，所以不会修改test.code的值