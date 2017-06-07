classmates = ['wuchen' , '蒙尘', 'ouyo']  #list是一种有序的集合
print(classmates)

print(len(classmates))  #len()函数可以获得list元素的个数

print(classmates[0])    #用索引来访问list中每一个位置的元素，索引是从0开始的

#print(classmates[3])   #超出索引范围，就会报索引越界的错误

print(classmates[-1])   #用-1做索引，直接获取最后一个元素,代表倒数第一个

print(classmates[-2])   #同理，倒数第二个，倒数依旧不能越界

#list是一个可变的有序表
classmates.append('孔子') #往list中追加元素到末尾
print(classmates)

classmates.insert(1,'老子')   #添加到索引为1的位置，后面的元素往后顺延
print(classmates)

classmates.pop()        #删除末尾的元素
print(classmates)

classmates.pop(1)       #删除指定位置的元素
print(classmates)

classmates[1] = '老臣'   #替换指定位置的元素
print(classmates)

L = ["苹果", 123 , True]  #元素也可以是不同的数据类型
print(L)

S = ['python', 'java', ['asp', 'php']]  #list元素也可以是另一个list
print(S)
