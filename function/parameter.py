'''定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。
对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了'''

#位置参数
def power (x):  #一个计算x的二次方的函数
   return x * x
print(power(5))

def power (x, n):   #修改后的power(x, n)函数，可以计算任意n次方
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5, 3))
'''修改后的power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，
    调用函数时，传入的两个值按照位置顺序依次赋给参数x和n
    新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，
    原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用：'''


#默认参数
'''由于我们经常计算x的平方，所以，完全可以把第二个参数n的默认值设定为2：'''
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(2)) #此时，当我们调用power(5)时，相当于调用power(5, 2)
print(power(5, 3))  #对于n>2的其他情况，就必须明确地传入n
'''设置默认参数时，有几点要注意：
1.必选参数在前，默认参数在后，否则Python的解释器会报错
2.当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。
  变化小的参数就可以作为默认参数
'''

#举例：写个一年级小学生注册的函数，需要传入name和gender两个参数：
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)
enroll('chen', '男') #此时，调用enroll()函数只需要传入两个参数

'''如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。
我们可以把年龄和城市设为默认参数：'''
def enroll(name, gender, age=6, city='beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

#这样，大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数：
enroll('chenchen', '男')

#只有与默认参数不符的学生才需要提供额外的信息：
enroll('liuliu', '女', 7)
enroll('yanyan', '女', city='nanjing')
'''有多个默认参数时，调用的时候，既可以按顺序提供默认参数，
比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，
最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，
需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，
意思是，city参数用传进去的值，其他默认参数继续使用默认值。'''

#踩坑举例
def add_end(L=[]):   #传入list做参数
    L.append('END')
    return L
print(add_end([1, 2, 3]))   #正常调用，没有问题
print(add_end())    #默认参数调用，暂时没有问题
print(add_end())    #结果出错，L的值被改变了，牢记一点，默认参数必须指向不可变对象

def add_end(L=None):    #使用None这个不变对象实现，无论调用多少次，都不会有问题了
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())

#可变参数
'''在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，'''
def calc(numbers):  #由于参数个数不确定，首先想到可以把a，b，c……作为一个list或tuple传进来
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1, 2, 3]))  #计算a2 + b2 + c2 + ...=,这样写虽然解决了问题，但是代码不够简化

#所以我们使用可变参数作为函数的参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2, 3))

#如果已经有一个list或tuple,要调用一个可变参数
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))  #繁琐的做法
print(calc(*nums))  #简单的做法，加一个*号，代表把list或tuple的元素变成可变参数传进去

#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name , age , **kw):
    print('name:', name, 'age:', age, 'other:', kw)
#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数
person('chenchen', 22)
#也可以传入任意个数的关键字参数
person('lala', 30 , city='beijing')
person('gaygay', 45, gender='女', job='Engineer')
'''关键字参数有什么用？
它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，
但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，
除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。'''

#上述代码亦有简化写法
extra = {'city':'beijing', 'job':'Engineer'}
person('Jack', 24, **extra)
'''**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。'''

#命名关键字参数
'''对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
至于到底传入了哪些，就需要在函数内部通过kw检查。
仍以person()函数为例，我们希望检查是否有city和job参数：'''
def person(name, age , **kw):
    if 'city' in kw:
        #有city参数
        pass
    if 'job' in kw:
        #有job参数
        pass
    print('name:',name, 'age:', age, 'other:', kw)
person('Jack', 24, city='beijing', addr='chaoyang', zipcode=123456) #调用者仍可以传入不受限制的关键字参数：

'''如果要限制关键字参数的名字，就可以用命名关键字参数，
例如，只接收city和job作为关键字参数。这种方式定义的函数如下：'''
def person(name, age, *, city, job):
    print(name, age , city, job)
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
person('jack', 24, city='beijing', job='houzi')

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
#person('chen', 24, 'beijing', 'houzi')
'''由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，
但person()函数仅接受2个位置参数。'''
def person(name, age, *, city='beijing', job):  #命名关键字参数可以有缺省值，从而简化调用：
    print(name, age , city, job)
#由于命名关键字参数city具有默认值，调用时，可不传入city参数
person('chen', 21, job='houzi')

'''
使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
'''
def person(name, age, city, job):
    #缺少*，city和job被视为位置参数
    pass

#参数组合
'''
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：
必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
比如定义一个函数，包含上述若干种参数：
'''
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)
#在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
f1(1,2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

#通过一个tuple和dict，你也可以调用上述函数
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的

'''Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。'''
