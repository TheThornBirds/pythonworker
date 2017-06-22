'''
当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
'''
'''
使用type()

首先，我们来判断对象类型，使用type()函数：

基本类型都可以用type()判断：
'''
print(type(123))    #int
print(type('str'))  #str
print(type(None))   #NonwType

print('--------------------')

'''
如果一个变量指向函数或者类，也可以用type()判断
'''
print(type(abs))    #builtin_function_or_method

'''
但是type()函数返回的是什么类型呢？它返回对应的Class类型。

如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
'''
print(type(123)==type(456)) #True

print(type(123)==int)   #True

print(type('abc') == str)   #True

print(type('abc') == type(123)) #False

print('--------------------')

'''
判断基本数据类型可以直接写int，str等，

判断一个对象是否是函数,可以使用types模块中定义的常量：
'''
import types
def fn():
    pass
print(type(fn) == types.FunctionType)   #True

print(type(abs) == types.BuiltinFunctionType)   #True

print(type(lambda x: x) == types.LambdaType)    #True

print(type((x for x in range(10))) == types.GeneratorType)  #True

print('--------------------')
'''
使用isinstance()

对于class的继承关系来说，使用type()就很不方便。

我们要判断class的类型，可以使用isinstance()函数。

isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
'''

'''
使用dir()

如果要获得一个对象的所有属性和方法，可以使用dir()函数，

它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
'''
print(dir('ABC'))


'''
仅仅把属性和方法列出来是不够的，

配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
'''
class myObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = myObject()

print('--------------------')
#紧接着，可以测试该对象的属性
print(hasattr(obj, 'x'))   #有属性x吗
print(obj.x)    #查看该属性的值
print(hasattr(obj, 'y'))    #有属性'y'吗
setattr(obj, 'y', 19)    #设置一个属性'y'
print(hasattr(obj, 'y'))    #有属性'y'吗
print(getattr(obj, 'y'))    #获取属性y
print(obj.y)    #获取属性'y'

'''
如果试图获取不存在的属性，会抛出AttributeError的错误：
'''
#print(getattr(obj, 'z'))    #获取属性'z'

'''
可以传入一个default参数，如果属性不存在，就返回默认值：
'''
print('--------------------')
print(getattr(obj, 'z', 404))   #获取属性'z'，如果不存在，则返回404

print('--------------------')
'''也可以获得对象的方法：'''
print(hasattr(obj, 'power'))    #有属性'power’吗？#True
print(getattr(obj, 'power'))    #获取属性power
fn = getattr(obj, 'power')  #获取属性'power'并复制到变量fn
print(fn)  #fn指向obj.power
print(fn())
print(obj.power())  #调用fn()和调用obj.power()是一样的

'''
小结

通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。

要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
sum = obj.x + obj.y

就不要写：
sum = getattr(obj,'x') + getattr(obj, 'y')

一个正确的用法例子如下：
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
'''

'''
假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，

如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上用场了

请注意，在python这种动态语言中，根据鸭子类型，有Read()方法，

不代表fp对象就是一个文件流，也可能是网络流，也可能是内存中的一个字节流，

但只要read()方法返回的事有效的图像数据，就不影响到读取图像的功能
'''


