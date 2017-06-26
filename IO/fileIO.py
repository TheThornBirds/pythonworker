'''
读写文件是最常见的IO操作。

Python内置了读写文件的函数，用法和C是兼容的
'''

'''
读文件
要以读文件的模式打开一个文件对象，

使用Python内置的open()函数，传入文件名和标示符：
'''

f = open('D:/test.txt', 'r')
#标示符'r'表示读，这样，我们就成功地打开了一个文件。
'''
如果文件不存在，open()函数就会抛出一个IOError的错误，

并且给出错误码和详细的信息告诉你文件不存在：

如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，

Python把内容读到内存，用一个str对象表示：
'''
print(f.read())

'''
最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，

因为文件对象会占用操作系统的资源，

并且操作系统同一时间能打开的文件数量也是有限的：
'''
try:
    f = open('D:/test.txt', 'r')
    print(f.read())
finally:
    if f :
        f.close()

'''
但是每次都这么写实在太繁琐，所以，

Python引入了with语句来自动帮我们调用close()方法：
'''
with open('D:/test.txt', 'r') as f:
    print(f.read())

'''
这和前面的try ... finally是一样的，

但是代码更佳简洁，并且不必调用f.close()方法。
'''

'''
小文件用read()
大文件用read(size)
配置文件用readlines()
'''

'''
二进制文件
要读取二进制二建，比如图片视频，用'rb'模式打开文件即可
'''
f = open('D:\chen.jpg', 'rb')
print(f.read()) # 会输出十六进制表示的字节

'''
字符编码
要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
'''
f = open('D:/test.txt','r',encoding='gbk')
print(f.read())

'''
open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。

最简单的方式是直接忽略
'''
f = open('D:/test.txt','r',encoding='gbk',errors='ignore')
print(f.read())


'''
写文件
写文件和读文件是一样的，唯一区别是调用open()函数时，

传入标识符'w'或者'wb'表示写文本文件或写二进制文件：

要写入特定编码的文本文件，应该给open()函数传入encoding参数，

将字符串自动转换成指定编码。
'''
with open('d:\wuchen.txt','w') as f:
    f.write('吴晨太帅')

'''
在Python中，文件读写是通过open()函数打开的文件对象完成的。

使用with语句操作文件IO是个好习惯。
'''