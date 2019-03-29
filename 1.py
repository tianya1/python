import random
inputval=int(input("1:,2:,3:"))
random=random.randint(0,2)
print(random)

if(inputval==0 and random==2) or (inputval==1 and random==0) \
    or (inputval==2 and random==1):
    print("%s"%random)
elif(inputval==0 and random==2):
    print('no')
else:
    print('yes')
    
################


i=0
res=0
while(i<101):
    if i%2==0:
       res+=i
    i+=1
print("结果为:%s"%res)

################
for i in range(1,10,2):
    print(i)
for i in range(1,10):
    print(i)
    
i=1
while i<6:
    j=0
    while j<i:
        print("* ",end="")
        j+=1
    i+=1
    print('\n')
################
i=1
while i<10:
    j=1
    while j<=i:
        print("%d * %d = %d" %(i,j,i*j),end=" ")
        j+=1
    print('\n')
    i+=1
################
import random
offices=[[],[],[]]
names=['a','b','c','d','e','f','g','h']
for name in names:
    index=random.randint(0,2)  # 0 1 2
    offices[index].append(name)
i=1
for temp in offices:
    print("办公室%d的人数为:%d"%(i,len(temp)))
    i+=1
    for name in temp:
        print("%s"%name,end='')
    print("-"*20)
################
def display_menu():
    print('-'*30)
    print("名片管理系统")
    print("1 添加名片")
    print("2 删除名片")
    print("3 修改名片")
    print("4 查询名片")
    print("5 获取名片信息")
    print("6 退出")
    print('-'*30)

def get_choice():
    key=int(input('input your choice'))
    return key

name_list=[]

def main():
    i=0
    while(i<1):
        display_menu()
        key=get_choice()
        if(key==1):
            add()
        elif(key==2):
            pass
        elif(key==3):
            pass
        elif(key==4):
            pass
        elif(key==5):
            pass
        elif(key==6):
            pass
        else:
            print('输入错误')
            break;

def add():
    name=input("输入姓名")
    name_list.append(name)


def showall():
    print("="*30)
    for info in name_list:
        print(info)
    print("="*30)
    
################ 

# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-03-29 09:46:10
# @Last Modified by:   Marte
# @Last Modified time: 2019-03-29 10:41:18

student_info=[]

def print_menu():
    print('-'*30)
    print('管理系统')
    print('1.添加')
    print('1.添加')
    print('1.添加')
    print('1.添加')
    print('1.添加')
    print('-'*30)

def add_info():
    name=input('输入姓名')
    sex=input('输入性别')
    phone=input('输入手机号码')
    new_info=[]
    new_info['name']=name
    new_info['sex']=sex
    new_info['phone']=phone
    student_info.append(new_info)


def del_info(stu):
    del_num=int(input('输入编号'))-1
    del stu[del_num]


def modify_info():
    stu_id=int(input('输入编号'))
    name=input('输入姓名')
    sex=input('输入性别')
    phone=input('输入手机号码')
    student_info[stu_id-1]['name']=name
    student_info[stu_id-1]['sex']=sex
    student_info[stu_id-1]['phone']=phone


def show_info():
    print('='*30)

    print('学生信息如下')

    print('='*30)

    print('序号 姓名 性别 电话')
    i=1
    for temp in (student_info):
        print("%d %s %s %s"%(i,temp['name'],temp['sex'],temp['phone']))
        i+=1

def main():
    while(True):
        print_menu()
        key=int(input('输入选项功能'))
        if(key==1):
            add_info()
        elif key==2:
            del_info(student_info)
        elif key==3:
            modify_info()
        elif key==4:
            show_info()
        elif key==0:
            confirm=input('确定要退出吗?Yes/No')
            if(confirm=='Yes'):
                break;
            else:
                print('输入错误')

################ 
res=map(lambda x,y:x+y,[1,2,3],[4,5,6])
print(list(res))

func=lambda x,y:x+y
res=(func,[1,2,3],[4,5,6])

func=lambda x:x%2
res=filter(func,[1,2,3,4,5,6])

func=lambda x,y:x+y
res=reduce(func,[1,2,3,4,5,6])

################ 

open()
close()
r w 
read()
write()
readline()
readlines()

old=input('输入文件名')
oldfile=open(old,"r")
if oldfile:
    flag=old.rfind('.')
    if flag>0:
        file_flag=old[flag:]
        new=old[:flag]+'[复件]'+file_flag

    newfile=open(new,"w")    
    for line in oldfile.readlines():
        newfile.write(line)
    newfile.close()
    
oldfile.close()

################ 
import os
os.rename('','')
os.remove('')

os.mkdir('')
os.rmdir('')
os.getcwd()

def print_menu():
    print('-'*30)
    print('管理系统')
    print('1.保存')
    print('-'*30)

student_info=[]

def save_file():
    file=open('backup.data','w')
    file.write(str(student_info))
    file.close()
#write方法只能传str数据

def recover_data():
    global student_info
    file=open('backup.data','r')
    content=file.read()
    student_info=eval(content)
    file.close()
#eval 恢复源数据到制定类型

################ 
模块  包  init.py
if __name__=='__main__':
    add()

################ 

    

    
    
    
    
