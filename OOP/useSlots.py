class Student(object):
    pass

s = Student()
s.name = 'Michael' #动态给实例绑一个属性
print(s.name)

def set_age(self, age): #定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)   #给实例绑定一个方法
s.set_age(25)   #调用实例方法
print(s.age)    #测试结果

def set_score(self, score):
    self.score = score
Student.set_score = set_score   #给class绑定方法后，所有实例均可调用

'''
通常情况下，上面的set_score方法可以直接定义在class中，

但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
'''

'''
为了达到限制的目的，Python允许在定义class的时候，

定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
'''
class Student(object):
    __slots__ = ('name', 'age') #用tuple定义允许绑定的属性名称
'''试图绑定其他属性将得到AttributeError的错误。'''

'''
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，

对继承的子类是不起作用的,除非在子类中也定义__slots__，


这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
'''



