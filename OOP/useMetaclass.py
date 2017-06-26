'''
type()
动态语言和静态语言最大的区别，就是函数和类的定义
不是编译时定义的，而是运行时动态创建的
比如我们要定义一个Hello的class，就写一个hello.py的模块：
'''
class Hello(object):
    def hello(self, name = 'world'):
        print('Hello,%s.' %name)
'''
当Python解释器载入hello模块时，就会依次执行该模块的所有语句，
执行结果就是动态创建出一个Hello的class对象，测试如下：
'''
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

