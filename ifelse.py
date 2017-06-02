age = 20           #如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做
if age >= 18:
    print("your age is", age)
    print('棒棒棒')

age = 3            #如果if判断是False，不要执行if的内容，去执行else
if age >=18:
    print('your age is ', age)
    print('666')
else:
    print('your age is ', age)
    print('还太小')

age = 3            #使用elif做更细致的判断，elif是else if的缩写
if age >= 18:
    print('成年了')
elif age >= 6:
    print("乖乖上学去")
else:
    print('oh baby')

x = 1        #只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if x:
    print('true')
#if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else，

'''
birth = input('birth: ')    #直接输入数字会报错，因为这里input()返回类型是Str,str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情
if birth < 2000:
    print('00前')
else:
    print('00后')
'''
#针对上面被注释掉的代码做出以下改动
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')


'''练习

小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：'''

height = 1.75
weight = 80.5
bmi = (weight/(height * height))
if bmi < 18.5:
    print('太瘦')
elif bmi <= 25:
    print('继续保持')
elif bmi <= 28:
    print('过重')
elif bmi <= 32:
    print('肥胖')
elif bmi > 32:
    print('再不减肥就没人爱了')

