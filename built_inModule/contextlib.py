'''
实现上下文管理是通过__enter__和__exit__这两个方法实现的。

例如，下面的class实现了这两个方法：
'''
class Query(object):
    def __init__(self, name):
        self.name = name
    def __enter__(self,):
        print('Begin')
        return self
    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' %self.name)

'''
这样我们就可以把自己写的资源对象用于with语句：
'''
with Query('Bob') as q:
    q.query()