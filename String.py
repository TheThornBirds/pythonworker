
print(ord('中'))     #字符整数表示
print('\u4e2d\u6587')#中文
print('ADC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(len('ADC'))   #计算字符数
print(len(b'adc'))  #计算字节数
print('hello,%s' %'world')  #格式化方式，%d代表整数，%f代表浮点数，%s代表字符串,%x代表十六进制数
print('hi,%s,you have $%d.' %('wuchen' , 100000000))    #有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
print('%d-%02d' % (3 , 1))  #补0
print('%.2f' % 3.1415926)   #保留两位小数
print('age: %s. Gender: %s' %(25 , True))   #%s会把任何数据类型转换为字符串
print('growth rate: %d %%' %7)  #%%来表示一个%

#小明的成绩从去年的72分提升到了今年的85分，计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位
s1 = 72
s2 = 85
r = (s2 - s1)/s1*100
print('小明成绩提升的%.1f%%'%r)

