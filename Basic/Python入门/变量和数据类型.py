# 整数：十六进制用 0x 前缀和 0-9，a-f 表示，例如：0xff00, 0xa5b7cd7...
#
# 浮点数：把10用e代替，1.23x10^9 就是 1.23e9，或者 1.23e8，0.000012 可以写成 1.2e-5
#
# 布尔值：一个布尔值只有 True、False 两种值（注意大小写）
#
# 空值：用 None 表示。


# 0x12fd2 这里是16进制，转换成10进制是：77778
# 10进制转换成16进制的方法是，1*16^4 + 2*16^3 + f*16^2 + d*16^1 + 2*16^0
print(456789 + 0x12fd2)
print('Learn Python in PhpZhi')
print(100 < 99)
print(0xff == 255)

# Python 用','进行字符串的连接
print('The quick brown fox', 'jumps over', 'the lazy dog')
print('100 + 200 =', 100 + 200)

# Python 中的变量

# 例子：等差数列可以定义为第一项与它的前一项的差等于一个常数，可以用变量x1表示等差数列的第一项，用d表示公差，请计算数列 1 4 7 10 13 16 19 前 100 项的和。
x1 = 1
d = 3
n = 100
xn = x1 + (n - 1) * d
s = ((x1 + xn) * n) / 2
print(s)

# Python 中定义字符串
print('Python was started in 1989 by "Guido".')
print('Python is free and easy to learn.')
print('Hello, I say, "I\'m a Python learner".')

# Python 中Unicode字符串
print('可以在第一行添加注释： # -*- coding: utf-8 -*-')
print(u'中文')

# Python 中整数和浮点数
print(11 / 4)
print(11 % 4)
print(2.5 + 10 / 4)

# Python 中的布尔类型
a = 'Python'
print('hello,', a or 'world')
b = ''
print('hello,', b or 'world')
