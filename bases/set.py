#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复

s = set([1, 2, 3])    #要创建一个set，需要提供一个list作为输入集合
print(s)

s = set([1, 1, 2, 2, 3])    #重复元素在set中自动被过滤
print(s)

s.add(4)    #通过add(key)方法可以添加元素到set中
print(s)

s.add(4)    #可以重复添加，但不会有效果
print(s)

s.remove(4) #通过remove(key)方法可以删除元素
print(s)

s1 = set([1, 2, 3]) #set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1|s2)

#扩展，不可变对象
#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的
a = ['c', 'b', 'a']
a.sort()
print(a)

#对于不可变对象,变量a最后仍是'abc'
a = 'abc'
b = a.replace('a', 'A')
print(b)
print(a)
'''要始终牢记的是，a是变量，而'abc'才是字符串对象！
有些时候，我们经常说，对象a的内容是'abc'，但其实是指，a本身是一个变量，
它指向的对象的内容才是'abc当我们调用a.replace('a', 'A')时，
实际上调用方法replace是作用在字符串对象'abc'上的，
而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，
变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：'''



