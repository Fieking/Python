# 这是第一个python文件,也是学习笔记
# 注意到 print 是一个函数
print ("Hello World")

# 数字: 分为整数(int)和浮点数
print (2) #这是一个整数例子
print (3.23,52.13E-4) #这是一个浮点数例子

#字符串: 字符串(String)是字符(Characters)的序列(Sequence).基本上字符串就是一串词汇.
# 单引号,框内的文本将按照原样保留
print ('框我,框我') 
# 双引号 和单引号作用一样.
print ("我在看言叶之庭")
# 三引号 可以使用"""或'''来指定多行字符串.三引号之就可以自由使用单引号和双引号.
''' 这是一段多引号的例子
This is the secoud line.
"What's your name?", I asked.
He said "Bond,James Bond."
'''
# ps: 字符串不可改变.

# 格式化方法
# 例子: str_format.py
age = 20
name = 'Swaroop'

print ('{0} was {1} years old when he wrote this book'.format(name,age)) 
print ('Why is {0} palying with that python?'.format(name)) 
# 以此类推
name + 'is' +str(age) + 'years old'
# 数字不是必要的 
age = 20 
name = 'Swaroop'

print ('{} was {} years old when he wrote this book'.format(name,age))
print ('Why is {} playing with that python?'.format(name))
# 这是精简数字之后的例子.
# format 方法所做的事情就是将每个参数值替换至格式所在位置.这之中可以有更详细的格式,例如:
# 对于浮点数 '0.33' 保留到小数点(.)后三位
print ('{0:3f}'.format(1.0/3))
# 使用下划线填充文本,并保持文字处于中间位置
# 使用(^)定义 '__hello__'字符串的长度为11
print ('0:_^11'.format('hello'))
# 基于关键字输出 'Swaroop wrote A Byte of Python'
print ('{name} wrote {book}'.format(name='Swaroop', book='A byte of Python'))

# print 总会以一个不可见的"新一行"字符(\n)结尾,防止这个情况可以使用end指定其应以空白结尾:
print('a'.end='\n')
print('b'.end='\n')
# 其输出结果为ab
# 或者通过 end 指定以空格结尾:
print('a'.end=' ')
print('b'.end=' ')
print('c')
# 其输出结果:a b c

# 转义序列(待续)