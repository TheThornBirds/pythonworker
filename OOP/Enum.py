'''
枚举类
当我们需要定义常量时，一个办法是用大写变量通过整数来定义，
好处是简单，缺点是类型是int , 并且仍然是变量，
更好的方法为这样的枚举类型定义了一个class类型，然后
每个敞亮都是class的一个唯一实例。
python提供了Enum类来实现这个功能：
'''
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr',
                       'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

'''
此时我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量
或者枚举他的所有成员:
value属性则是自动赋给成员的int常量，默认从1开始计数。
'''
for name, member in Month.__members__.items():
    print(name,'=>', member, ',', member.value)

'''如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：'''
from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0 #sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

'''
@unique装饰器可以帮助我们检查保证没有重复值,
访问这些枚举类型可以有若干种方法
'''
print('-----')

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))
print(day1 == Weekday(1))
for name , member in Weekday.__members__.items():
    print(name, '=>', member)

'''
Enum可以把一组相关常量定义在一个class中，

且class不可变，而且成员可以直接比较。
'''