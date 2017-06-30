# 我们先编写hello.py,实现web应用程序的wsgi处理函数：
# xixi.py
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello,web!</h1>']