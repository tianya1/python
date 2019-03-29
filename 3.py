#socket网络编程  见w3c课程

import socket
import sys
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
serversocket.bind((host, port))
serversocket.listen(5)
while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()
    print("连接地址: %s" % str(addr))
    msg='欢迎访问W3Cschool教程！'+ "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()

####################
import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
s.connect((host, port))
msg = s.recv(1024)
s.close()
print (msg.decode('utf-8'))
########################


#SMTP发送邮件




#多线程


import threading
import time
exitFlag = 0
class myThread(threading.Thread):
    def __init__(self,threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")


#迭代器
#生成器

#迭代器有两个基本的方法：iter() 和 next()。

list=[1,2,3,4]
it = iter(list)
print (next(it))

for x in it:
    print (x, end=" ")

while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()

#使用了 yield 的函数被称为生成器（generator）
#在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，
#返回yield的值。并在下一次执行 next()方法时从当前位置继续运行。
#


import sys
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()

##########
def fun():
    n=1
    while True:
        if n>3:
            #return
            break
        print(n)
        n+=1

fun()


#数据结构


#XML解析  


#json解析

json.dumps(): 对数据进行编码。
json.loads(): 对数据进行解码。

#使用 threading 模块创建线程

import json
# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'W3CSchool',
    'url' : 'http://www.w3cschool.cn'
}

json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)

#repr() 函数将对象转化为供解释器读取的形式。
#dict = {'runoob': 'runoob.com', 'google': 'google.com'};
#repr(dict)
#"{'google': 'google.com', 'runoob': 'runoob.com'}"


data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])

# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)

# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)
    

爬虫

