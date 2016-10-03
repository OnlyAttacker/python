#coding=utf-8

#错误：
#1、语法错误：代码不符合解释器或者编译器语法
#2、逻辑错误：不完整或者不合法输入或者计算出现的问题

#异常：执行过程中出现问题导致程序无法执行
#1、程序遇到逻辑或者算法问题
#2、运行时计算机出现的问题（内存不够，权限不够等）

#python常见错误
#1、NameError :没有定义变量则引用该变量
#print a #报错：NameError: name 'a' is not defined

#2、SyntaxError	#运行前异常，无法捕获
#if a	#报错：SyntaxError: invalid syntax，程序无法捕获该异常

#3、IOError
#f = open('test.txt') #IOError: [Errno 2] No such file or directory: 'test.txt'

#4、ZeroDivisionError
#10/0  #ZeroDivisionError: integer division or modulo by zero

#5、ValueError
#a = int('a') #ValueError: invalid literal for int() with base 10: 'a'
#6、KeyboardInterrupt

#import time
#for i in range(10):
#	time.sleep(2) #在运行中使用^C来终止程序运行，会出现KeyboardInterrupt错误



# try-except:异常处理

# try:
# 	try_suite
# except [Exception [,e]]:
# 	exception_block

# 实例：
# try:
# 	a
# except NameError,e:
# 	print e 	#name 'a' is not defined
# print 'exec over'

# 当except后指定了异常，
# 但是不是抛出的异常，
# 此时，不会捕获该异常

# try-except：处理多个异常
# try:
# 	try_suite
# except Exception1[,e]:
# 	exception_block
# except Exception2[,e]:
# 	exception_block

# try-except--else使用
# try:
# 	try_suite
# except Exception[,e]:
# 	exception_block
# else:
# 	none_exception

# try-finally:使用,无论是否检查到异常都会去执行finally
# 主要用于资源清理工作

# try:
# 	try_suite
# except Exception[,e]:
# 	exception_block
# else:
# 	none_exception
# finally:
# 	do_finally

#####try-finally用法1
# import sys
# try:
# 	f = open('test.txt')
# except IOError,e:
# 	print "file not exist"
# 	sys.exit(1)

# try:
# 	num = f.read();
# 	print int(num)
# except ValueError,e:
# 	print 'ValueError'
# else:
# 	print "no error"
# finally:
# 	print "close file execute"
# 	f.close()

#####try-finally用法2 
#finally中还得使用一下try-except
# try:
# 	f = open('test.txt')
# 	int(f.read())
# except IOError,e:
# 	print "file not exist"
# except ValueError,e:
# 	print 'ValueError'
# else:
# 	print "no error"
# finally:
# 	try:
# 		print "close file execute"
# 		f.close()	#防止文件打开错误
# 	except NameError,e:
# 		print e

# python 中with语句
# with context [as var]:
# 	with_suite
# context表达式返回的是一个对象
# try:
# 	with open('text.txt') as f:
# 		print f.read()
# except IOError,e:
# 	print e

# with语句实质是上下文管理：
# 1、上下文管理协议：
# 支持该协议对象要实现这两个方法__enter__()和__exit__()

# 2、上下文管理器：定义执行with语句时要建立的运行时上下文，
# 负责执行with语句块上下文中的进入和退出操作。
# 3、进入上下文管理器：
# 调用管理器__enter__方法，如果设置了as var语句，var变量接受__enter__方法返回值
# 4、退出上下文管理器：
# 调用管理器__exit__方法

# class MyContext(object):
# 	def __init__(self,name):
# 		self.name = name

# 	def __enter__(self):
# 		print "__enter__"
# 		return self
# 	def do_self(self):
# 		print "do_self"

# 	def __exit__(self,exc_type,exc_value,traceback):
# 		print "__exit__"
# 		print "exc_type:%s\nexc_value:%s\ntraceback:%s\n" % (exc_type,exc_value,traceback)

# if __name__ == "__main__":
# 	with MyContext("test") as t:
# 		print t.do_self()


#结果如下：
# __enter__
# do_self
# None
# __exit__
# exc_type:None
# exc_value:None
# traceback:None

#with语句应用场景：
# 1、文件操作
# 2、进程线程之间互斥对象，例如互斥锁
# 3、支持上下文的其他对象

# raise语句和assert语句
# raise用于抛出异常
# assert用于检查表达式是否为真，
# 如果为假，引发AssertionError错误
# raise语法
# raise [exception[,args]]
# exception:异常类
# args:描述异常信息的元祖
# try:
# 	raise IOError,"file not found"
# except IOError,e:
# 	print e  #输出file not found

# assert语法
# assert expression[,args]
# expression : 表达式
# args：判断条件的描述信息
# try:
# 	assert 1==2,"error"
# except AssertionError,e:
# 	print e 	#输出error

# python标准异常和自定义异常
# 标准异常：python内建异常
# BaseException 所有异常基类 
# Exception 继承BaseException，常见错误的基类
# KeyboardInterrupt 继承BaseException，用户中断（ctrl+c）
# SystemExit 继承BaseException，Python解释器退出

# SyntaxError，NameError，IOError，ImportError...都是继承Exception的
# 自定义异常继承Exception类或其子类
# class FileError(IOError):
# 	pass
# try:
# 	raise FileError,"file not found"
# except Exception, e:
# 	print e













