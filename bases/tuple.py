classmates = ('刘刘', '晨晨', 'charles')    #tuple和list类似，但是tuple一旦初始化就不能修改
print(classmates)

t = ()  #定义一个空的tuple

t = (1,) #定义只有一个元素的tuple必须加一个逗号，消除歧义
print(t)

t = ('a', 'b', ['A', 'B'])  #"可变"的tuple,这里变得不是tuple的元素，而是list的元素。
t[2][0] = 'x'
t[2][1] = 'y'
print(t)

#练习:用索引取出下面list的指定元素：
# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
print(L[-1][-1])

