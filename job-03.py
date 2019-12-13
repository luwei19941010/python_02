#-*-coding:utf-8-*-
# Author:Lu Wei

count=1
sum=0
while count<11:
    if count == 7:
        count+=1
        continue
    else:
        print(count)
        count += 1


for count in range(10):
    if count ==7:
        pass
    else:
        count += 1
        print(count)

count4=1
while count4 <101:
    sum=sum+count4
    count4+=1
print(sum)

c=1
while c<101:
    a=c%2
    if a==1:
        print(c)
        c+=1
    else:
        c+=1

d=1
while d<101:
    D=d%2
    if D==0:
        print(d)
        d+=1
    else:
        d+=1
sum=0
e=1
while e <100:
    E=e%2
    if E==1:
        sum=sum+e
        e+=1
    else:
        sum=sum-e
        e += 1
print(sum)



username='luwei'
password='123'
#user=input('请输入用户名:')
#psd=input('请输入密码:')
count=2
while count!=-1:
    user = input('请输入用户名:')
    psd = input('请输入密码:')
    print('login count %s'%count)
    if user==username and psd==password:
        print('ok')
    else:
        count-=1

#ACSLL   1字节
#UNICODE 4字节
#UTF-8   1-4字节

#8bit=1byte,1024byte=1KB

print( 1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# T
print( not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# F

print(8 or 3 and 4 or 2 and 0 or 9 and 7)
#8
print(0 or 2 and 3 and 4 or 6 and 0 or 3)
#4

print(6 or 2 > 1)
#6
print(3 or 2 > 1)
#3
print(0 or 5 < 4)
#F
print(5 < 4 or 3)
#3
print(2 > 1 or 6)
#T
print(3 and 2 > 1)
#T
print(0 and 3 > 1)
#0
print(2 > 1 and 3)
#3
print(3 > 1 and 0)
#0
print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)
#2
