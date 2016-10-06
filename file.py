#coding=utf-8
#python文件操作
# 文件：Python中文件是对象
# linux文件：一切设备都可以看成文件
# 例如：磁盘文件，管道，网络Socket，外设等
# 文件属性：用户，读、写、执行权限

# python文件打开方式
# 文件打开方法：open(name[,mode[,buf]])
# name:文件路径
# mode:打开方式（只读，只写，读写）
# buf：缓冲buffering大小

# 文件读取方式:
# read([size]):读取文件（读取size个字节（不够则读取全部），默认读取全部）
# readline([size]):读取一行
# readlines([size]):读取完文件(若文件很大时，读取完buff个字节)，返回每一行所组成的列表
# iter:使用迭代器读取大文件
##################################################
# 默认buff大小
# import io
# print io.DEFAULT_BUFFER_SIZE	#8192
##################################################
###########文件很大时，不建议全部读取#############

# 文件写入方式
# write(str):将字符串写入文件
# writelines(sequence_of_strings):写多行到文件

# python文件打开方式
# mode	说明			注意
# 'r'		只读方式打开	文件必须存在
# 'w'		只写方式打开	文件不存在则创建文件，文件存在则清空文件内容
# 'a'		追加方式打开	文件不存在创建文件
# 'r+'/'w+'读写方式打开	
# 'a+'	追加和读写方式打开
# 在后面加上b则以二进制方式打开 例如 'rb','rb+','ab+'
# f = open('test.txt','w+')
# f.writelines(['sdf\n','sdfsfd'])
# f.close()
# f = open('test.txt','r')
# content = f.readlines()
# for i in content:
# 	print i

# 使用迭代器读取大文件（因为文件缓存大小有限制，无法使用readlines()读取全部文件）
# f = open('test.txt')
# iter_f = iter(f)
# lines = 0
# for line in iter_f:
# 	lines += 1
# 	print lines
# 	print line

#文件为什么要关闭
# 1、将写缓存同步到磁盘；可用flush()或close()将不足缓存的内容写到磁盘。
# 2、linux系统中每个进程打开文件的个数是有限的
# 3、如果打开文件数到了系统限制，再打开文件就会失败

# 首先ps 查看python进程号，然后cat /proc/python_pid/limits 查看进程中的限制
# 每打开一个文件都会有一个file.fileno() 文件号

# 文件指针，读取和写入文件时公用一个指针，指向读取和写入位置的指针
######################## 注意：#######################
# 使用f.read(2) 读两个字节后，指针向后移动，此时再写入时会出错，
# 必须使用seek来重新定义指针位置再写才不会出错
######################################################
# 可使用seek(offset[,whence]):移动文件指针
# offset ：偏移量，可为负数
# whence：便宜相对位置
# Python 文件指针定位方式
# os.SEEK_SET 相对文件起始位置
# os.SEEK_CUR 相对文件当前位置
# os.SEEK_END 相对文件结尾位置


# 例子1
# import os
# f = open('test.txt','w+') #以什么mode打开文件，则指针会位置可能会不同
# f.write('test')
# f.seek(2,os.SEEK_SET)
# f.write('test')		#会把后面st的覆盖
# f.close()

# 例子2
# import os
# f = open('test.txt','w+') #以什么mode打开文件，则指针会位置可能会不同
# f.write('test')
# f.seek(0,os.SEEK_SET)
# print f.read(2)	#写完后，读两个字节，然后再写时会出错 此时必须使用seek来调整一下指针
# print f.tell()  #打印出文件指针的位置 输出2
# f.seek(2,os.SEEK_SET)
# f.write('test')	
# f.close()

# Python 文件属性
# file.fileno() 	文件描述符
# file.mode 		文件打开模式
# file.encoding 	文件编码
# file.closed 		文件是否关闭
# f = open('test.txt')
# print f.fileno()
# print f.mode
# print f.encoding
# print f.closed
# f.close()

# python标准文件
# 文件标准输入：sys.stdin
# 文件标准输出：sys.stdout
# 文件标准错误：sys.stderr
# import sys
# print type(sys.stdin)	#输出 <type 'file'>
# print sys.stdin.mode	#输出 r
# print sys.stdin.fileno()#输出 0
# ##################################################################
# ### 也就是启动一个进程后，首先打开一个标准输入，从控制台读入数据
# # ##################################################################

# # 这里输入字符回车后，将输出输入的第一个字符
# print sys.stdin.read(1)	#从标准输入流读入一个字节 
# #################################################

# sys.stdout.write('test') #控制台输出 test
# sys.stderr.write('test') #控制台输出 test,出现错误时也是打到控制台的
# print sys.stdout.fileno()#输出 1
# print sys.stderr.fileno()#输出 2

# python 文件命令行参数
# sys模块提供sys.argv属性，通过这个属性可以得到命令行参数
# sys.argv:字符串组成的列表
# print sys.argv #输出调用这个脚本的绝对路径，也就是第一个参数

# python 文件编码格式
# 使用普通方式打开文件：写入u'高'，会出现什么问题
# f = open('test.txt','r+')
# f.write('123')
# f.write(u'高')	#UnicodeEncodeError 'ascii' codec can't encode character u'\u9ad8' 
# 				#in position 0: ordinal not in range(128)
# f.close()

#可以将unicode转化为utf-8再写入
# a = unicode.encode(u'高','utf-8') 
# #unicode一个汉字占两个字节 utf-8一个汉字占三个字节
# f = open('test.txt','w+')
# f.write(a)
# f.close()

# 创建一个utf-8或其他编码格式文件
# 使用codecs模块提供方法创建指定编码格式文件
# open(fname,mode,encoding,errors,buffering):使用指定编码格式打开文件
# import codecs
# f = codecs.open('test.txt','w','utf-8')
# print f.encoding #输出utf-8
# f.write('高')
# f.close()

# 使用os模块打开文件，更偏向于linux系统调用
# os.open(filename,flag[,mode])
# os.O_CREATE：创建文件
# os.O_RDONLY：只读方式打开
# os.O_WRONLY：只写方式打开
# os.O_RDWR：读写方式打开

# os.read(fd,buffersize):读取文件
# os.write(fd,string):写入文件
# os.lseek(fd,pos,how):文件指针操作
# os.close(fd) 关闭文件







