# Single line comments start with a hash.
# 单行注释由一个井号开头。
""" Multiline strings can be written
    using three "'s, and are often used
    as comments
    三个双引号（或单引号）之间可以写多行字符串，
    通常用来写注释。
"""

####################################################
## 1. Primitive Datatypes and Operators
## 1. 基本数据类型和操作符
####################################################

# You have numbers
# 数字就是数字
3 #=> 3

# Math is what you would expect
# 四则运算也是你所期望的那样
1 + 1 #=> 2
8 - 1 #=> 7
10 * 2 #=> 20
35 / 5 #=> 7

# Division is a bit tricky. It is integer division and floors the results
# antomatically.
# 除法有点棘手
# 对于整数除法来说，计算结果会自动取整。
5 / 2 #=> 2

# To fix division we need to learn about floats.
# 为了修正除法的问题，我们需要先学习浮点数。
2.0    # This is a float
2.0    # 这是一个浮点数
11.0 / 4.0 #=> 2.75 ahhh...much better
11.0 / 4.0 #=> 2.75 啊...这样就好多了

# Enforce precedence with parentheses
# 使用小括号来强制计算的优先顺序
(1 + 3) * 2 #=> 8

# Boolean values are primitives
# 布尔值也是基本数据类型
True
False

# negate with out
# 使用 not 来取反
not True #=> False
not False #=> True

# Equality is ==
# 等式判断用 ==
1 == 1 #=> True
2 == 1 #=> False

# Inequality is !=
# 不等式判断是用 !=
1 != 1 #=> False
2 != 1 #=> True

# More comparisons
# 还有更多的比较运算
1 < 10 #=> True
1 > 10 #=> False
2 <= 2 #=> True
2 >= 2 #=> True

# comparisons can be chained!
# 居然可以把比较运算串联起来！
1 < 2 < 3 #=> True
2 < 3 < 2 #=> False

# strings are created with " or'
# 使用"或' 来创建字符串
"This is a string."
'This is also string.'

# strings can be added too!
# 字符串也可以相加！
"Hello" + "world!" #=> "Hello world!"

# A string can be treated like a list of characters
# 一个字符串可以视为一个字符的列表
# （译注：后面会讲到“列表”）
"This is a string"[0] #=> 'T'

# % can be usede to format strings,like this:
# % 可以用来格式化字符串，就象这样：
%s can be %s % ("strings","interpolated")

# A newer way to format strings is the format method.
# This method is the preferred way
# 后来又有一种格式化字符串的新方法：format 方法
# 我们推荐使用这个方法。
"{0} can be {1}".format("strings","formatted")

# You can use keywords if you don't want to count.
# 如果你不喜欢数数的话，可以使用关键字（变量）。
"{name} wants to eat {food}".format(name="Bob",food="lasagna")

# None is an object
# None 是一个对象
None #=> None

# Don't use the equality `==` symbol to compare objects to None
# Use `is` instead
# 不要使用相等符号 `==` 来把对象和 None 进行比较，
# 而要用 `is`。
"ect" is None #=> False
None is None #=> True

# The `is` operator tests for object identity. This isn't
# very useful when dealing with Primitive values,but is
# very useful when dealing with objects.
# 这个 `is` 操作符用于比较两个对象的标识。
# （译注：对象一旦建立，其标示就不会改变，可以认为它就是对象的内存地址。）
# 在处理基本数据类型是基本用不上，
# 但它在处理对象是很有用。

# None, 0, and empty strings/lists all evaluate to False.
# All other values are True
# None、0 以及空字符串和空列表都等于`False,
# 除此以外的所有值都等于 True。
0 == False #=> True
"" == False #=> True


####################################################
## 2. Variables and Collections
## 2. 变量和集合
####################################################

# Printing is pretty easy
# 打印输出很简单
print "I'm Python. Nice to meet you!"

# No need to declare variables defore assigning to them.
# 在赋值给变量值钱不需要声明
some_var = 5 #Convention is to use lower_case_with_underscores
             # 变量名的约定是使用下划线分隔的小写单词
some_var #=> 5

# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
# 访问一个未赋值的变量会产出一个异常
# 进一步了解异常处理，可参看下一节《控制流》
some_other_var # Raises a name error
               # 会抛出一个名称错误

# if can be used as an expression
# if 可以作为表达式来使用
"yahoo!" if 3 > 2 else 2 #=> "yahoo!"

# Lists store sequences
# 列表用于存储序列
li = []
# You can start with a prefilled list
# 我们先尝试一个预先填充好的列表
other_li = [4, 5, 6]

# Add stuff to the end of a list with append
# 使用 append 方法把元素添加到列表的尾部
li.append(1)    #li is now [1]
li.append(2)    #li is now [1, 2]
li.append(4)    #li is now [1, 2, 4]

