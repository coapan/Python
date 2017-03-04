# List 类型，例如：['A', 'B', 'C']
L = ['A', 'B', 'C']

# 访问 List
print(L[0])
print(L[1])
print(L[2])

# 倒序访问 List
print(L[-1])
print(L[-2])
print(L[-3])

# List 添加新元素
# 添加到末尾
L.append('D')
print(L)
# 添加到任意位置
L.insert(0, 'D')
print(L)

# Python 从List删除元素, pop()会直接删除最后一个元素
# 可以给 pop() 指定参数
L.pop()
print(L)
L.pop(3)
print(L)

# tuple 是另一种有序的列表，tuple一旦创建完毕，就不能修改，但是List可以修改
t = ('Admin', 'Root', 'Localhost')  # 用 （）代替掉了 []
print(t)

t = (1, 2, 3,)
print(t)

t = ('a', 'b', 'c', ['1a', '2b', '3c'])
print(t)
L = t[3]
print(L)
L[0] = '111'
L[1] = '222'
L[2] = '333'
print(t)
