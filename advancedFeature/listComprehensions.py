'''
列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
'''
print(list(range(1, 11)))   #生成1到10的list

#生成1x1,2x2...
L = []
for x in range(1, 11):  #方法一：循环
    L.append(x * x)
print(L)

print([x * x for x in range(1 , 11)]) #方法2：列表生成式

#for循环后面还可以加上if判断
print([x * x for x in range(1, 11) if x % 2 == 0])  #筛选仅为偶数的平方

#两层循环生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])    #第一个是外层循环，第二个是内层循环

import  os # 导入os模块
print([d for d in os.listdir('.')])    # 列出当前目录下的所有文件和目录名

d = {'x': 'A', 'y': 'B', 'z': 'C'}  #for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
for k, v in d.items():
    print(k,'=',v)

# 因此，列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for  k, v in d.items()])

# 把一个list中所有的字符串变成小些：
L = ['HELLO', 'World', 'IBM', 'APPLE']
print([s.lower() for s in L])

'''
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：

>>> L = ['Hello', 'World', 18, 'Apple', None]
>>> [s.lower() for s in L]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <listcomp>
AttributeError: 'int' object has no attribute 'lower'
使用内建的isinstance函数可以判断一个变量是不是字符串：

>>> x = 'abc'
>>> y = 123
>>> isinstance(x, str)
True
>>> isinstance(y, str)
False
请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
'''
L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])