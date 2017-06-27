'''
操作文件和目录
Python内置的os模块也可以直接调用操作系统提供的接口函数。
'''
import os
print(os.name)  # 操作系统类型

'''
如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
'''

'''
环境变量
在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
'''
print(os.environ)

'''
要获取某个环境变量的值，可以调用os.environ.get('key')：
'''
print(os.environ.get('PATH'))

'''
操作文件和目录
'''
print('-----\n')

print(os.path.abspath('.')) #查看当前目录的绝对路径

#首先把新目录的完整路径表示出来:
print(os.path.join('E:/pythonworker/IO', 'testdir'))

#然后创建一个目录：
#os.mkdir('E:/pythonworker/IO/testdir')

#删掉一个目录
#os.rmdir('E:/pythonworker/IO/testdir')

'''
把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，

拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数

这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名

os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
'''
print('-----\n')

print(os.path.split('E:/pythonworker/IO/file.txt'))
print(os.path.splitext('E:/pythonworker/IO/file.txt'))

'''
这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
'''
print('-----\n')
#os.rename('file.txt', 'test.py')   #对文件重命名
#os.remove('test.py')    #删除文件

'''利用python特性过滤文件，比如列出当前目录下所有目录'''
print('-----\n')
print([x for x in os.listdir('.') if os.path.isdir(x)])

'''列出所有的.py文件'''
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

