d = {'a': 1, 'b': 2, 'c': 3}
for key in d:       #迭代dict的key
    print(key)

for value in d.values():    #迭代dict的value
    print(value)

for k, v in d.items():  #同时迭代key和value
    print(k,v)

for ch in 'ABC':    #迭代字符串
    print(ch)

'''
如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
'''
from collections import Iterable
print(isinstance('abc', Iterable)) #判断str是否可以迭代
print(isinstance([1,2,3],Iterable)) #判断list是否可以迭代
print(isinstance(123, Iterable))    #判断整数是否可以迭代

'''
Python内置的enumerate函数可以把一个list变成索引-元素对，
这样就可以在for循环中同时迭代索引和元素本身
'''
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)