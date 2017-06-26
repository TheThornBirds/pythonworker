'''
BUG的处理
'''
'''
try
'''
try:
    print('try...')
    r = 10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
'''不走try就走except,最后走finally，所有错误类型继承自BaseException'''






