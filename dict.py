#dict关于其他语言的map,dict的key必须是不可变对象,是无序的

d = {'wuchen':92, 'liuming':75, 'lanzhou':85}   #dict使用键-值（key-value）存储,直接根据名字查找成绩
print(d['wuchen'])

d['wuchen'] = 67       #通知key值放入值，并且一个key只能对应一个value，如果重复对一个key放入value，后者会冲掉前者
print(d['wuchen'])


'''print(d['charles'])  #如果key不存在，则会报错,为避免错误，可以使用下面两种方法'''

print('charles' in d)   #可以使用in判断key是否存在

print(d.get('charles')) #如果key不存在，则返回none,或者自己指定的value
print(d.get('charles',-1))

d.pop('lanzhou')    #删除一个key,对应的value也会从dict中删除
print(d)

