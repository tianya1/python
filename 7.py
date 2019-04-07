python函数式编程
高阶函数

函数指向变量
f=abs
map()
reduce()
filter()
sorted()
闭包  返回函数

匿名函数

@fun
装饰器decorator函数
无参数decorator  有参数decorator

#闭包
def count():
    fs = []
    for i in range(1, 4):
        def f(i):
            return lambda : i*i
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())


def count1():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count1()
print(f1(),f2(),f3())

############
def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn
@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)

########
def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kw)
    return fn
    
@log
def add(x, y):
    return x + y
print add(1, 2)

###########
def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def test():
    pass
print test()
########

import functools
def log(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
    
########

functools.partial  创建一个偏函数

import functools
int2 = functools.partial(int, base=2)
int2('1000000')

######
from __future__ import unicode_literals

s = 'am I an unicode?'
print isinstance(s, unicode)

from __future__ import division

#######

