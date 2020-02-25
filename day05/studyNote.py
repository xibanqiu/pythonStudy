#数据类型划分：可变数据类型  不可变数据类型
#不可变数据类型  ： 元组  bool int str       --> 可哈希
#可变数据类型   list ，dict  set            --->不可哈希

'''
dict： key  必须是不可变数据类型 ，可哈希
       value  :任意数据类型
     优点：二分查找去查询
            存储大量的关系型数据
            特点：无序性
'''
#案例
dic ={
    'name':['小明','小红'],
    'py9':[{'num',71,'avg_age',18},
           {'num',70,'avg_age',21},
           ],
    True:1,
    (1,2,3):'wudi',
    2:'er',
}
dic1 = {'height' : 18 ,
        'width' : 1  ,
        }

#增加
'''
dic1['height'] = 16 #如果有键值对 ，则覆盖
print(dic1)

dic1['high'] = 100   #如果没有 ，则添加
print(dic1)

dic1.setdefault('age',150)  #有键值对 ，不做任何改变，没有才添加
print(dic1)
'''

#删除
'''
print(dic1.pop('height'))  #按键去删除，有返回值
print(dic1.pop('age',"没有值啊"))  #按键去删除，可以设置返回值 。如果没有会报错

print(dic1.popitem()) #随机删除 有返回值 是元组中删除的键值

del dic1['height']  #按键去删除  没有值会报错，返回键值对
print(dic1)
del dic1       #删除字典

dic1.clear()   #清空
'''

#改
'''
#根据 key 修改值
dic1['width'] = 16

#update 没有的键  
dic = {
    "name":"jin",
    "age":"18",
    "sex":"male",
}
dic2 = {
    "name":"alex",
    "weight":"180",
}

dic2.update(dic)
print(dic)   #{'name': 'jin', 'age': '18', 'sex': 'male'}
print(dic2)  #{'name': 'jin', 'weight': '180', 'age': '18', 'sex': 'male'}

'''

#查
'''
dic = {
    "name":"jin",
    "age":"18",
    "sex":"male",
}
print(dic.keys(),type(dic.keys()))
print(dic.values())
print(dic.items())

for i in dic:
    print(i)

for i in dic.keys():
    print(i)

for k,v in dic.items():
    print(k,v)


i=dic['age']
print(i)

print(dic.get('age','没有这个值'))
print(dic.get('aaa','没有这个值'))

'''