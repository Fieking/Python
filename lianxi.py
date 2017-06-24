# 数据类型和变量 测试代码

n = 123
print('n=',n)
f = 456.789
print('f=',f)
s1 = 'Hello, world'
print('s1=',s1)
s2 = "'Hello,\\'Adam\\''"
print('s2=',s2)
s3 = "r'Hello,\"Bart\"'"
print('s3=',s3)
s4 = "r'''Hello,"+"\nLisa!'''"
print('s4=',s4)

# 字符和编码 测试代码

# -- coding: utf-8 --
s1 = 72
s2 = 85
c = (1-s1/s2)*100
print('\'%02d,%.1f%%\'' % (s2,c))

# list 是列表

classmates = ['Michael','Bob','Tracy']
classmates
