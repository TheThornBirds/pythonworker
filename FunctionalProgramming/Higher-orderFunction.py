'''
高阶函数
'''

# 变量可以指向函数
x = abs(-10)
print(x)

f = abs     # 变量可以指向函数。并且可以通过该变量来调用这个函数
print(f(-10))

#函数名也是变量
'''
函数名其实就是指向函数的变量！
对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！
'''
# abs = 10
# print(abs(-10))
'''
把abs指向10后，就无法通过abs(-10)调用该函数了！

因为abs这个变量已经不指向求绝对值函数而是指向一个整数10！

当然实际代码绝对不能这么写，这里是为了说明函数名也是变量。

要恢复abs函数，请重启Python交互环境。
'''

#传入函数
'''
既然变量可以指向函数，函数的参数能接收变量，
那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
'''
def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6 , abs))

#把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

#map/reduce
'''
map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
'''
def f(x):   #激素那list中每一个数的平方
    return x * x
r = map(f, [1, 2, 3 ,4, 5, 6, 7, 8, 9])
print(list(r))

print(list(map(str, [1, 2, 3])))    #把这个list所有数字转为字符串

#reduce
'''
把一个函数作用在一个序列上，reduce把结果继续和序列的下一个元素做累积计算
'''
from functools import reduce
def add(x , y): #对一个序列求和,当然求和可以直接使用sum()函数实现。
    return x+y
print(reduce(add, [1, 3, 5]))

from functools import reduce
def fn(x, y):   #把序列[1, 3, 5, 7, 9]变换成整数13579
    return x * 10 + y
print(reduce(fn, [1, 3, 5]))

from functools import  reduce
def fn(x, y):   #把str转换为int的函数
    return x * 10 + y
def char2num(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,
            '6':6, '7':7, '8':8, '9':9}[s]


print(reduce(fn, map(char2num, '13579')))

from functools import  reduce
def str2int(s): #整理成一个str2int的函数
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
print(str2int('12345'))

'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
'''
def normalize(name):
    return name[0].upper()+name[1:].lower()
L1 = ['adam', 'LISA', 'BARt']
L2 = list(map(normalize, L1))
print(L2)

'''
请编写一个prod()函数，可以接受一个list并利用reduce()求积
'''
from operator import mul
def prod(L):
    def fn(x, y):
        return x*y
    return reduce(fn,L)
print(prod([1, 2 ,3]))


#filter
'''
filter()也接收一个函数和一个序列,把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。
'''
def is_odd(n):  #在一个list中，删掉偶数，只保留奇数
    return n % 2 ==1
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 9])))

def not_empty(s):   #把一个序列中的空字符串删掉
    return s and s.strip()
print(list(filter(not_empty, ['a', '', 'b', None, 'c', ' '])))
'''
filter()函数返回的是一个Iterator，也就是一个惰性序列，
所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
'''

#sorted
print(sorted([36, 5, -12, 9, -21])) #Python内置的sorted()函数就可以对list进行排序

print(sorted([36, 5, -12, 9, -21], key=abs))    #还可以接收一个key函数来实现自定义的排序
#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序



