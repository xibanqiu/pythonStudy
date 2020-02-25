'''
list,查询过程中修改，会报错，类似java的并发修改异常

Traceback (most recent call last):
  File "C:/1xubenqing/python/myCode/study1/day07/studyNote.py", line 11, in <module>
    del lis[i]
IndexError: list assignment index out of range

lis=[11,22,33]
for i in lis:
    del lis[i]

'''



'''
集合：可变的数据类型，他里面的元素必须是不可变的数据类型，无序，不重复

set1 = set({1,2,3});
print(set1)

#set2 = {1,2,3,[2,3],{'name':'alex' }}  #错误 列表 和 字典的 是可变数据类型
'''
set1 = {'alex','wusir','ritian','egon','barry','barry'}
### 增加
'''
set1.add('女神')
print(set1)  #{'女神', 'barry', 'egon', 'wusir', 'alex', 'ritian'}
set1.update('abd')
print(set1)  #{'a', 'alex', 'ritian', 'barry', 'wusir', 'egon', 'd', 'b'}

'''

###删除
'''
set1.pop() #随机删除,有返回值
print(set1)  # {'ritian', 'wusir', 'barry', 'alex'}

set1.remove('alex') # 按元素删除
print(set1)

set1.clear()  #清空集合

del set1   #删除集合
'''

### 查
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

### &
'''
set3  = set1 & set2
print(set3)  #print(set3)
print(set1.intersection(set2)) #print(set3)   
'''

### |
print( set1 | set2)  #{1, 2, 3, 4, 5, 6, 7, 8}
print(set2.union(set1))  #{1, 2, 3, 4, 5, 6, 7, 8}


### ^
print( set1 ^ set2)  #{1, 2, 3, 6, 7, 8}
print( set1.symmetric_difference(set2) ) #{1, 2, 3, 6, 7, 8}


###
print(set1.difference(set2))  #{1, 2, 3}


set3 = {1,2,3,}
set4 = {1,2,3,4,5,6}
print(set1 < set2)
print(set1.issubset(set2)) # 这两个相同

print(set1 > set2)
print(set1.issuperset(set2)) # 这两个相同