def counter(start_at=0):
       count = start_at
       while True:
           val = (yield count)
           if val is not None:
               count = val
           else:
               count += 1

count = counter(5)
print(type(count))
print(next(count))
count.send(9)
print(next(count))
count.close()
print(next(count))


def odd():
    n=1
    while True:
        yield n
        n+=2
odd_num = odd()
count = 0
for o in odd_num:
    if count >=5: break
    print(o)
    count +=1


#大文件读取
read()  readline()  readlines()


def test1():    with open("/tmp/test.log", "r") as f:        print f.read()   f.close()

def test2():    f = open("/tmp/test.log", "r")    for line in f.readlines():        print line    f.close()

def read_in_block(file_path): 
    BLOCK_SIZE = 1024
    with open(file_path, "r") as f: 
        while True: 
            block = f.read(BLOCK_SIZE) 
             if block: 
                yield block
             else:
                 return
                 
def test3():
    file_path = "/tmp/test.log"    
    for block in read_in_block(file_path):        
        print block


def test4():    
    with open("/tmp/test.log") as f:        
        for line in f:            
            print line                   
###############
