############
#  dict 是什么
d = {
    'Admin': 59,
    'Root': 95,
    'Localhost': 57,
    'Pan': 98
}

len(d)

# dict 的访问
print(d['Admin'])

if 'Pan' in d:
    print(d['Pan'])

print(d.get('Localhost'))
print(d.get('Local'))

# dict 的特点  1、查找速度快 2、没有顺序 3、元素不可变 4、占用内存大
print(d)

# dict 的更新
d['PanChao'] = 57
print(d)
d['Pan'] = 100
print(d)

# dict 的遍历
for key in d:
    print(key + ':', d[key])

##########
#  Python 中的set  创建set的方式是调用 set() 并传入一个list，list的元素将作为set的元素：
# set的元素没有重复，而且是无序的，set会自动去年重复的元素
L = ['A', 'B', 'C', 'D']
s = set(L)
print(s)

# 访问set，注意区分大小写
print('D' in s)
print('d' in s)
print('F' in s)

# set的特点
# 判断一个元素是否在set中的速度很快
# 任何可变对象是不能放入set中
# set存储的元素是没有顺序的

# 例子：判断用户输入的某个数是否是有效的
L = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
weekdays = set(L)

i = 'TUE'
if i in weekdays:
    print('thank you')
else:
    print('Please try again later')

# set 的遍历
L = [('MON', 90), ('TUE', 59), ('WED', 69), ('THU', 78)]
weekdays = set(L)
for name in weekdays:
    print(name[0] + ':', name[1])

# set 的更新
L = [1, 2, 3]
s = set(L)
s.add(5)
print(s)

s.add(3)  # 添加相同元素
print(s)

s.remove(3)  # 删除一个元素
print(s)

s.remove(8)  # 删除不存在的元素会报错
print(s)

# 所以用add()可以直接添加，而 remove() 前需要判断
