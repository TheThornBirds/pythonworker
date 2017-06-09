'''
在Python中，这种一边循环一边计算的机制，称为生成器：generator
'''

# 第一种方法，只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x * x for x in range(10)]
print(L)
G = (x * x for x in range(10))
print(next(G)) #一个一个打印出来，通过next函数获得下一个打印值
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

g = (x * x for x in range(10))  #迭代generator
for n in g:
    print(n)

def fib(max):   # 定义斐波拉契，如果一个函数定义中包含yield关键字，它就是一个generato
    n, a, b = 0, 0, 1
    while n < max:
        yield (b)
        a, b = b, a+b
        n = n +1
    return 'done'
for n in fib(6):
    print(n)

g = fib(6)
while True:
    try:
        x = next(g)
        print('g', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
for n in triangles():
    print(n)