#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
'''
举个例子，我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：

fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n

所以，fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理。

于是，fact(n)用递归的方式写出来就是
'''
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(998))
