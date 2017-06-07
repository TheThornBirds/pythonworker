'''Python内置了很多有用的函数，我们可以直接调用。

要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。

可以直接从Python的官方网站查看文档：

http://docs.python.org/3/library/functions.html#abs'''

print(abs(100)) #调用abs函数，求绝对值，只接受一个参数，类型不可以是字符

print(max(1, 2))    #max()可以接受多个参数，并返回最大的那个

print(int('123'))   #int()函数，把其他数据类型转换为整数
print(int(12.34))

print(float('12'))   #float()函数，把其他数据类型转换为浮点数

print(str(1.23))    #str()函数，把其他数据类型转换为字符串

print(bool(2))     #bool()函数，把其他数据类型转换为布尔值
print(bool(''))

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(-1))