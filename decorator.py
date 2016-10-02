#coding=utf-8
#先假设一个场景
#输入数学，语文，英语等的成绩（输入的门数不定）
#有几个函数
#grade_avg 求成绩平均分
#grade_sum 求成绩总分

#必须对输入的参数做判断

#初步的程序，没有做输入参数判断
# def grade_avg(*args):
# 	return sum(args)/len(args)

# def grade_sum(*args):
# 	return sum(args)

#由于两个函数的参数判断是相同的逻辑，
#所以直接在两个函数里面写，有点代码冗余

#于是使用函数闭包的特性来解决，
#主要是因为python，javascript等语言中可以将一个函数当作一个变量来传递
#主要思路：
#	将这个函数传递到另一个函数中，
#	另一个函数对这个函数进行判断，
#	然后再返回跟这个函数具有相同功能的函数，并且具有函数判断逻辑
#	从而实现对这两个函数都加上参数判断逻辑

def args_check(func):
	def closing(*args):
		if len(args) == 0:
			return 0
		for val in args:
			if not isinstance(val,int):
				return 0
		return func(*args)
	return closing


# def grade_avg(*args):
# 	return sum(args)/len(args)

# def grade_sum(*args):
# 	return sum(args)

# grade_sum = args_check(grade_sum)
# grade_avg = args_check(grade_avg)
# print grade_sum(1,2,3)
# print grade_avg(1,2,3,'')



# 语法糖
#grade_avg = args_check(grade_avg)
@args_check
def grade_avg(*args):
	return sum(args)/len(args)

# 语法糖
#grade_sum = args_check(grade_sum)
@args_check
def grade_sum(*args):
	return sum(args)


print grade_sum(1,2,3)
print grade_avg(1,2,3,'')

#装饰器的原理
#调用函数args_check来给传入的函数重新封装成一个函数，返回这个函数
#之后再调用返回的这个函数，从而实现调用装饰后的函数








