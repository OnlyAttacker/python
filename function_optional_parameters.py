#coding=utf-8

#python中如果想要只传其中几个且不按照从左往右的顺序，则在调用函数时只需传 参数名=参数值
def optional_parameter(a=1,b=2):
    print a,b

if __name__ == '__main__':
    optional_parameter(b=22)    #输出 1 22



