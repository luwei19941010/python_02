### day02

##### 昨天内容回顾

```
昨日内容回顾：   
python2x 与 python3x区别:        
		python2x:源码重复，不规范，默认编码ASCII，代码首行 %-*-encoding:utf-8-*-。        				python3x:源码规范，优美，清晰，简单，默认编码UTF-8。    
编译型：将代码一次性全部转化成字节码        
			代表型：C，C+        
			优点：执行速度快        
			缺点：不能跨平台，开发速度慢    
解释型：代码从上至下逐行解释。        
			代表语言：python        
			优点：开放效率高，便于调式，可以跨平台        
			缺点：执行速度低    
			python：Cpython，Jpython，Ironpython，pypy...
```





##### 1.字符串格式化

%占位符

1.%s,

2.%d,

3.%%

```
template='我是%s,年龄%d,职业%s。'%('luwei',25,'network')

name='luwei'

template='%s的手机的电量是100%%'%(name,)
print(template)
```

##### 2.运算符

![image-20191212131652973](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20191212131652973.png)

数字转布尔值

```
v1=0
v2=bool(v1)
print(v2)
-----> false  #只有0位false
```

字符串转布尔值

```
v1=''
v2=bool(v1)
print(v2)
----->false  #只有‘空’为false
```

对于or用法：

​		第一个值如果是转换布尔值如果是真，则value=第一个值。
​		第一个值如果是转换布尔值如果是假，则value=第二个值。
​		如果有多个or条件，则从左到右依次进行上述流程。

```
value=1 or 9
---->1
value=0 or 9
---->0
value=0 or ''
---->''
```



对于and用法：

​		如果第一个值转换成布尔值是True，则value=第二个值。
​		如果第一个值转换成布尔值是False，则value=第一个值。
​		如果有多个and条件，则从左到右依次进行上述流程。

```
v1=1 and 9
---->9
v2=1 and 0
---->0
v3=0 and 10
---->0
v4=0 and ''
---->0
```



综合来看优先级（）> not > and > or。

```
   v1=1 and 9 or 0 and 6
-->v1=9 or 0 and 6
-->v1=9 or 0
-->v1=9
```



##### 3.编码

- ascii（1字节）

- unicode（4字节）

  - ecs2
  - ecs4

- utf-8（1-4字节）中文3个字节

- utf-16

- GBK 中文2个字节

- GB2312 中文2个字节

  

  字节单位

  ![image-20191212200959146](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20191212200959146.png)

  

##### 4.Git

​	步骤：

1. git init

2. git add . 

3. git commit -m '第x天作业'

   ```
   第一次执行时，需要执行
   git config --global user.email "davidlu1994@163.com"
   git config --global user.name "陆威"
   ```

4. git remote add orgin https://gitee.com/luwei1994/Python_01.git

5. git push orgin1 master



其他

git status 查看当前目录下所有问题

git add . 收集当前目录下所有问题

git commit -m ‘03’ 给当前目录写下提交记录

git push origin master



 