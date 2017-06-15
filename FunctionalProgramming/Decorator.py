#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
    print('2015-3-25')
f = now
f()

#函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)

'''
假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
本质上，decorator就是一个返回函数的高阶函数
'''
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' %func.__name__)
        return func(*args, **kw)
    return wrapper
'''
因为它是一个decorator，所以接受一个函数作为参数，
并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处
'''
print("--------------------------")
@log
def now():
    print('2015-3-25')

now()   #调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
now = log(now)  #把@log放到now()函数的定义处，相当于执行了这条语句

'''
#装饰器这里不太好理解，，下面是我找来的例子
def foo():
    print('i am foo')
#现在有一个新的需求，希望可以记录下函数的执行日志，于是在代码中添加日志代码
def foo():
    print('i am foo')
    logging.info("foo is running")

bar(), bar2()也有类似的需求应该怎么做呢？再写一个logging在bar函数里吗？
这样就造成了大量雷同代码，为了减少重复写代码，我们可以这样做，重新定义一个函数：
专门处理日志，日志处理完之后再执行真正的业务代码

def use_logging(func):
    logging.warn("")
    func()

def bar():
    print('i am bar')

use_logging(bar)


逻辑上不难理解，但是这样的话，每次都要将一个函数作为参数传递给use_logging函数
，而且这种方式已经破坏了原有的代码逻辑结构，之前执行业务逻辑时，执行运行bar(),
但是现在不得不改称use_logging(bar).我们应该使用更好的方式，也就是装饰器


#简单装饰器
def use_logging(func):
    def wrapper(*args, **kwargs):
        logging.warn("%s is running" %func.__name__)
        return func(*args, **kwargs)
    return wrapper()

def bar():
    print('i am bar')

bar = use_logging(bar)
bar()


函数use_logging就是装饰器，它把执行真正业务方法的func包裹在函数里面，
看起来像bar被use_logging装饰了。在这个例子中，函数进入和退出时 ，
被称为一个横切面(Aspect)，这种编程方式被称为面向切面的编程(Aspect-Oriented Programming)。
@符号是装饰器的语法糖，在定义函数的时候使用，避免再一次赋值操作

def use_logging(func):
    def wrapper(*args, **kwargs):
        logging.warn("%s is running" %func.__name__)
        return func(*args, **kwargs)
    return wrapper()

@use_logging    #等同于上面那一段赋值操作
def bar():
    print('i am bar')

bar()


如上所示，这样我们就可以省去bar = use_logging(bar)这一句了，
直接调用bar()即可得到想要的结果。如果我们有其他的类似函数，
我们可以继续调用装饰器来修饰函数，而不用重复修改函数或者增加新的封装。
这样，我们就提高了程序的可重复利用性，并增加了程序的可读性。

装饰器在Python使用如此方便都要归因于Python的函数能像普通的对象一样,
能作为参数传递给其他函数，
可以被赋值给其他变量，可以作为返回值，可以被定义在另外一个函数内。



带参数的装饰器
装饰器还有更大的灵活性，例如带参数的装饰器：在上面的装饰器调用中，
比如@use_logging，该装饰器唯一的参数就是执行业务的函数。
装饰器的语法允许我们在调用时，提供其它参数，比如@decorator(a)。
这样，就为装饰器的编写和使用提供了更大的灵活性。

def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" %func.__name__)
            return func(*args)
        return wrapper
    return decorator

@use_logging(lever = "warn")
def foo(name='foo'):
    print("i am %s" % name)
foo()

上面的use_logging是允许带参数的装饰器。它实际上是对原有装饰器的一个函数封装，
并返回一个装饰器。我们可以将它理解为一个含有参数的闭包。
当我 们使用@use_logging(level="warn")调用的时候，
Python能够发现这一层的封装，并把参数传递到装饰器的环境中。

'''