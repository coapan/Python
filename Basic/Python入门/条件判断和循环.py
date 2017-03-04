# Python 的if语句
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

score = 75
if score >= 60:
    print('Passed')
    print('Bart\'s score is', score)

# Python 的if-else语句
age = 12
if age >= 18:
    print('adult')
else:
    print('teenager')

# Python 的if-elif-else语句
age = 100
if 40 > age >= 18:
    print('adult')
elif 60 > age >= 40:
    print('high')
elif age >= 60:
    print('very old')
else:
    print('teenager')

# Python 中的for循环
L = ['1s', '2a', '3c']
for name in L:
    print(name)

# 循环计算平均值
L = [75, 92, 59, 68]
s = 0.0
for rs in L:
    s = (s + rs)
print(s / 4)

# Python 中的while循环
N = 10
M = 0
while M < N:
    print(M)
    M = (M + 1)

# 循环嵌套
for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        print(x + y)
