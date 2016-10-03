#coding=utf-8
#正则表达式
# 1、python正则表达式模块
import re

# 2、第一个正则表达式
# 注意：
# 	生成Pattern对象，不能够自己实例化，
#   只能通过re.compile()生成

#####正则顺序如下：
# #####
# 1、通过正则模块re.compile()生成Pattern对象
# 2、Pattern对象使用match方法匹配字符串，生成Match对象
# 3、Match对象使用group()返回匹配的结果

# r'test'->Pattern(Pattern对象)->Match(Match对象)->result(Match.group()得到结果)
#Python中的原始字符串以r开头,使用原始字符串可以避免字符串中转义字符带来的问题
pattern = re.compile(r'test')	#前面加r 表示字符串不需要转义，例如re.compile('test\n')不加r的话会把\n转义后再匹配
string = 'test.sdfsdftest'
print pattern.match(string).group()

#正则表达式语法
############ 匹配单个字符的表达式###############
# . 匹配除\n之外的所有字符
# \s / \S 匹配空白/非空白
# \d / \D 匹配数字/非数字
# \w / \W 匹配单词字符[a-zA-Z0-9]/非单词字符
# [...] 匹配[]中的字符，例如[a-z]匹配所有的小写字母

############# 匹配字符的次数####################
# *	匹配前一个字符0-n次
# +   匹配前一个字符1-n次
# ?   匹配前一个字符0或1次
# {m}/{m,n} 匹配前一个字符m次/匹配前一个字符m-n次
# *?/+?/?? 匹配模式变为非贪婪模式（尽可能少的匹配字符）

##############匹配字符串的边界##################
# 1、^匹配字符串的开始
# 2、$匹配字符串的结尾

##############正则表达式的分组##################
# 1、| 匹配左右任意一个表达式
# 2、(ab) 括号中座位一个分组
# 3、\<number> 因为编号为number的分组匹配到的字符串，常用语正则替换中
# 4、(?P<name>) 分组起一个别名
# 5、(?P=name) 引用别名为name的分组匹配到的字符串

############ match和search区别##################
#match()函数只检测RE是不是在string的开始位置匹配，
#search()会扫描整个string查找匹配；

###############################################################################
#注意 search和match都不是负责匹配所有的匹配结果，
#它们的共性就是能不能匹配出正则表达式的结果
#只不过match是从字符串的头开始匹配正则，而search是在整个字符串匹配正则
#匹配所有的是通过findall来实现的
###############################################################################

pattern = re.compile(r's$')	
string = '11sssssssasdjsdsssKJLSss'
print pattern.search(string).group()

pattern = re.compile(r'test')
print pattern.findall('testsstest')

############上面方式能实现正则表达式的重用######
################################################
################################################


############可以直接使用re来进行正则匹配########
# re.search(pattern, string, flags=0)
# 在字符串中查找，是否能匹配正则表达式。返回_sre.SRE_Match对象，如果不能匹配返回None。
# re.match(pattern, string, flags=0)
# 字符串的开头是否能匹配正则表达式。返回_sre.SRE_Match对象，如果不能匹配返回None。
# re.split(pattern, string, maxsplit=0)
# 通过正则表达式将字符串分离。如果用括号将正则表达式括起来，那么匹配的字符串也会被列入到list中返回。maxsplit是分离的次数，maxsplit=1分离一次，默认为0，不限制次数。
# re.findall(pattern, string, flags=0)
# 找到 RE 匹配的所有子串，并把它们作为一个列表返回。这个匹配是从左到右有序地返回。如果无匹配，返回空列表。
# re.sub(pattern, repl, string, count=0, flags=0)
# 找到 RE 匹配的所有子串，并将其用一个不同的字符串替换。可选参数 count 是模式匹配後替换的最大次数；count 必须是非负整数。缺省值是 0 表示替换所有的匹配。如果无匹配，字符串将会无改变地返回。
# re.subn(pattern, repl, string, count=0, flags=0)
# 与re.sub方法作用一样，但返回的是包含新字符串和替换执行次数的两元组。
print re.findall(r't',',testsstest')
print re.sub(r't','t1',',testsstest')
print re.subn(r't','t1',',testsstest')
