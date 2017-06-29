'''
hashlib
摘要算法又称哈希算法，散列算法，通过一个函数，把任意长度的数据转换为一个长度固定的数据穿
通常用16进制的字符串表示
'''

'''
摘要算法就是通过摘要函数对任意长度的数据data计算出固定长度的摘要
目的是为了发现原始数据是否被人篡改过
摘要算法之所以能指出数据是否被篡改，就是因为摘要算法是一个单向函数
计算f(data)很容易，但通过digest反推data却非常困难，而且
对原始数据做一个bit的修改，都会导致计算出的摘要完全不同

以常见的MD5为例，计算出一个字符串的md5值
'''
import hashlib

md5 = hashlib.md5()
md5.update('I AM WUCHEN'.encode('utf-8'))
print(md5.hexdigest())

'''
如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
'''
md5 = hashlib.md5()
md5.update('I AM '.encode('utf-8'))
md5.update('WUCHEN'.encode('utf-8'))
print(md5.hexdigest())
'''
只要改动一个字母，哪怕改动一个空格，计算结果也会完全不同
MD5是最常见的摘要算法，速度很快，声称结果是固定的128bit字节，
通常有一个32位的16进制字符串表示

另一种常见的摘要算法是SHA1，用法与MD5完全类似
'''
print('-----\n')

import hashlib
sha1 = hashlib.sha1()
sha1.update('I AM WUCHEN'.encode('utf-8'))
print(sha1.hexdigest())

'''
SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。

比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
'''

'''
摘要算法应用
任何允许用户登陆的网站都会存贮用户登陆的用户名和口令，方法就是存到数据表

如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。

此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。

正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：

当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，

如果一致，说明口令输入正确，如果不一致，口令肯定错误。
'''

'''
练习

根据用户输入的口令，计算出存储在数据库中的MD5口令：
'''
print('-----\n')

import hashlib
md5 = hashlib.md5()
md5.update('123456'.encode('utf-8'))
password1 = md5.hexdigest()

def calc_md5(password):
    md51 = hashlib.md5()
    md51.update(password.encode('utf-8'))
    return md51.hexdigest()

def login(password):
    if calc_md5(password)==password1:
        return '登陆成功'
    else:
        return '滚犊子'
print(login('123456'))


