'''
Python的class中有许多有特殊用途的函数，可以帮助我们定制类。
'''
'''
__str__
我们先定义一个Student类，打印一个实例：
'''
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self): #定义好__str__()方法，返回一个好看的字符串
        return 'Student object (name: %s)' %self.name
    __repr__ = __str__
print(Student('Michael'))

'''
如果不用print，打印出来还是不好看,
直接显示变量调用的不是__str__()
而是__repr__(),二者区别是__str__()返回的是用户看到的字符串，
而__repr__()返回程序开发着看到的字符串
__repr__()是为调试服务的
解决方法是在定义一个__repr__()
通常二者代码一样，所以可以直接把__str__()写好之后赋值给__repr__()
'''

'''
__iter__
如果一个类要被用于for ... in 循环，就必须实现一个__iter__()方法，
该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环
例：斐波那契数列
'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 #初始化两个计数器a, b

    def __iter__(self):
        return self #实力本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b #计算下一个值
        if self.a > 100000: #退出循环的条件
            raise StopIteration()
        return self.a   #返回下一个值
for n in Fib():
    print(n)

'''
__getitem
Fib实例虽然能作用于for循环，看起来和list有点像，
但是把它当成list使用还是不行，比如取第五个元素就会发生错误
要表现的像list那样取出元素，需要实现__getitem__()方法:
'''
print('------')
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a
print(Fib()[0]) #现在就可以按照下表访问数列的任意一项了

print('------')
print(list(range(100))[1:10])   #list的切片方法也不适用于Fib实例

print('-----')
'''
是因为__getitem__()传入的参数可能是一个int,
也可能是一个切片对象slice,所以要做判断
'''
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):  #n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):    #n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >=start:
                    L.append(a)
                a, b = b, a + b
            return L
f = Fib()
print(f[0:5])
print(f[:10])

'''
__getattr__
正常情况下，当我们调用类的方法或者属性时，如果不存在，就会报错
'''
print('-----')

class Student(object):
    def __init__(self):
        self.name = 'wuchen'
s = Student()
print(s.name)
#print(s.score) 调用了不存在的score属性，所以报错
'''
要避免这个错误，除了可以加上一个score属性外，

Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。
'''
print('-----')

class Student(object):
    def __init__(self):
        self.name = 'mengchen'
    def __getattr__(self, attr):
        if attr == 'score':
            return 99

'''
当调用不存在的属性时，比如score，

python解释器会试图调用__getarrt__(self,'score)

来尝试获取属性，这样我们就有机会返回score的值：
'''
s = Student()
print(s.name)
print(s.score)
'''
__call__
一个对象实例可以有自己的属性和方法，

当我们调用实例方法时，我们用instance.method()调用

任何类，只需要定义一个__call__()，就可以直接对实例进行调用。
'''
print('-----')

class Student(object):
    def __init__(self,name):
        self.name = name
    def __call__(self):
        print('My name is %s.' %self.name)

#调用方式如下
s = Student('wumeng')
s()

'''
判断一个对象是否是可调用对象 callable()函数
'''
print('-----')

print(callable(Student('chen')))  #True
print(callable(max))    #True
print(callable([1,2,3]))    #False
print(callable(None))   #False
print(callable('str'))  #False

