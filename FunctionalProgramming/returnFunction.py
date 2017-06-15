'''
返回函数：
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
'''
def lazy_sum(*args):    #不返回求和的结果，而是返回求和的函数
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f)    #返回求和的函数
print(f())  #调用函数f时，才真正计算求和的结果

'''
在这个例子中，我们在函数lazy_sum中又定义了函数sum，
并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
这种称为“闭包（Closure）”的程序结构拥有极大的威力
当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
'''
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2) #f1()和f2()的调用结果互不影响

#闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1(),f2(),f3())   #返回的函数并没有立刻执行，而是直到调用了f()才执行