names = ['Michael', '儿子', '父亲']
for name in names:
    print(name)
#一种是for...in循环，依次把list或tuple中的每个元素迭代出来,for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum+x
print(sum)
#计算1-10的整数之和

a = list(range(5))  #range()函数可以生成一个整数序列，从0开始，到指定数字减一
print(a)

sum = 0             #计算一到一百相加
for x in range(101):
    sum = sum + x
print(sum)


sum = 0             #while循环，只要条件满足，就不断循环，条件不满足时退出循环
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

'''练习

请利用循环依次对list中的每个名字打印出Hello, xxx!：'''
L = ['晨儿', '花儿', '草儿']
for x in L:
    print('hello,',x)