'''定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
然后，在缩进块中编写函数体，函数的返回值用return语句返回。'''
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-5))

def nop():  #定义一个空函数，就是什么事情都不做的函数
    pass

age = 20    #pass还可以用在其他语句里，
if age >= 18:
    pass

'''print(my_abs(-5, 5)) #如果传的参数个数不对，python会自动检查出来'''

'''print(my_abs('a'))  #当传入的参数类型不对时，不会进行参数检查，会出错'''

'''def my_abs(x):  
    if not isinstance(x, (int, float)): #对参数进行检查，只允许整数和浮点数的类型，这里使用isinstance()实现
        raise  TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs('a'))  #如果传入错误的参数类型，函数就可以抛出一个错误：'''

import  math    #import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。
def move(x, y, step, angle=0):  #该函数可以返回多个值
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
print(move(100, 100, 60, math.pi / 6))  #其实返回的仍然是单一值，但是是一个tuple
