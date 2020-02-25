# input实现与用户的交互

# name = input("请输入名字")
# age = int(input("请输入年龄"))
#
#
# s = 'my name is %s,age is %d'%(name,age)
# print(s)


# 使用while循环输入 1 2 3 4 5 6 8 9 10

"""
count = 0
while count <= 10:
    print(count)
    count += 1"""

#优先级 ， （） > not > and > or
# and or  not

# print(2 > 1 and 1 < 4)    # True
# print(2 > 1 and 1 < 4 or 2 < 3 and 9 < 6 or 2 < 4 and 3 < 2 ) #True

# T or F
# print(3>4 or 4<3 and 1==1) # F
# print(1 < 2 and 3 < 4 or 1>2) # T
# print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1) # T
# print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8) # F
# print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6) # F
# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6) # F

# int ---> bool 非零转换成bool  True  0转换成bool是 False
'''
print(bool(2)) ;   #T
print(bool(-2))
print(bool(0))

print(int(True))
print(int(False))
'''


# x or y
print(2 or 1 < 3)