import itertools

res=itertools.count(10,2)

for i in res:
    print(i,end='')

res=itertools.cycle('ABCD')
repeat(10, 3) --> 10 10 10
chain('ABC', 'DEF') --> A B C D E F
compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9
ifilterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
izip('ABCD', 'xy') --> Ax By
izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-

tee(it, n) 
返回n个迭代器it的复制迭代器。

groupby([0, 0, 0, 1, 1, 1, 2, 2, 2]) --> (0, (0 0 0)) (1, (1 1 1)) (2, (2 2 2))

product('ABCD', repeat=2) --> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
permutations(p[, r]) 
去除重复的元素。 
permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
combinations(p, r) 
排序后去除重复的元素。 
combinations('ABCD', 2) --> AB AC AD BC BD CD
combinations_with_replacement() 
排序后，包含重复元素。 
combinations_with_replacement('ABCD', 2) --> AA AB AC AD BB BC BD CC CD DD
######################
import sys
def fab(max):
         n, a, b = 0, 0, 1
         while n < max:
             yield b
             a, b = b, a + b
             n = n + 1


f=fab(5)

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()

#大文件读取
def read_file(fpath): 
    BLOCK_SIZE = 1024 
    with open(fpath, 'rb') as f: 
        while True: 
            block = f.read(BLOCK_SIZE) 
            if block: 
                yield block 
            else: 
                return      
 ##################
 
 
