# 对List进行切片
L = ['Admin', 'Root', 'Pan']
# L[0:3]表示，从索引0开始，直到索引3为止，但不包括索引3
print(L[0:3])

# 倒序切片 倒数第一个元素的索引是-1
L = ['Adam', 'LIsa', 'Bart', 'Paul']
print(L[-3:-1])

# 对字符串进行切片
print('ABCDEFG'[:3])  # 取前三个
print('ABCDEFG'[-3:]) # 取后面三个
print('ABCDEFG'[::3]) # 隔三取一

# 字符串有个方法 upper() 可以把字符变成大写字母：
print('abcdfg'.upper())




# 迭代 就相当于for循环
# 在Python中，如果给定一个list或tuple，我们可以通过for循环遍历这个list或tuple，这种遍历我们称为迭代(lteration)

# 索引迭代
# 使用 enumerate()函数，我们可以在for循环中同时绑定索引index和元素name
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index,name in enumerate(L):
	print(index, '-', name)

# 迭代的第一个元素实际上是一个tuple
for t in enumerate(L):
	index = t[0]
	name = t[1]
	print(index, '-', name)

# 迭代dict的value
# 使用 values() 方法
d = {'Adam': 95, 'Lisa': 85, 'Bart':59}
print(d.values())
for value in d.values():
	print(value)

# 使用 itervalues() 方法 3不能用你敢信
# print(d.itervalues())