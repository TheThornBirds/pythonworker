'''
调试
'''
'''
1.使用print()把可能有问题的变量打印
2.断言，凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
'''
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10/n

def main():
    foo('0')
'''
assert的意思是，表达式n != 0应该是True，

否则，根据程序运行的逻辑，后面的代码肯定会出错。

如果断言失败，assert语句本身就会抛出AssertionError：

启动Python解释器时可以用-O参数来关闭assert
'''

'''
3.把print()替换为logging是第3种方式，和assert比，

logging不会抛出错误，而且可以输出到文件：
'''
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' %n)
print(10 / n)

'''
这就是logging的好处，它允许你指定记录信息的级别，

有debug，info，warning，error等几个级别，

当我们指定level=INFO时，logging.debug就不起作用了。

同理，指定level=WARNING后，debug和info就不起作用了。

这样一来，你可以放心地输出不同级别的信息，也不用删除，

最后统一控制输出哪个级别的信息。

logging的另一个好处是通过简单的配置，

一条语句可以同时输出到不同的地方，比如console和文件。
'''


