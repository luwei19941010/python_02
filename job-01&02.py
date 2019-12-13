#-*-coding:utf-8-*-
# Author:Lu Wei

'''
count =0
a=int(input('--->请输入理想数字:'))

while count <3:
    b=int(input('--->请输入猜测数字:'))
    if a > b:
        print('偏小了')
    elif a < b:
        print('偏大了')
    else:
        break
    count+=count
print('答案正确，%s'%(b))
'''

#0=<a=<100

count=0
x=0
y=100

def diff2():
    while True:
        c = int(input('--->DF-2请输入[0,100]理想数字:'))
        if c not in range(0, 101):
            print('请重新输入正确范围内数字')
            continue
        return c

def diff3():
    while True:
        c = int(input('--->DF-3请输入猜测数字,范围%s至%s:' % (x, y)))
        if c not in range(x, y+1):
            print('请重新输入正确范围内数字')
            continue
        return c

a = diff2()
while count<3:
    b=diff3()
    if b<a:
        count += 1
        x = b
        print('偏小了，范围%s至%s' % (x, y))
    elif b>a:
        count += 1
        y=b
        print('偏大了，范围%s至%s' % (x, y))
    else:
        print('答案正确，%s' % (b))
        break
print('GGGG')

