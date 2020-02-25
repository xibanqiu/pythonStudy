#### 列表
li = ['alex','wusir','egon','女神','taibai']

###增加的3种方法

'''
# append
li.append('日天')
li.append(1)

print(li)


#一个 有关 append 的 小功能

while 1 :
    username = input( ">>>")
    if(username.upper().strip() == 'Q') :
        break
    else:
        li.append(username)

print(li)

#insert
li.insert(4,'小明')


#extend
li.extend('而且')

print(li)

'''

###删除的方法
'''
#pop
name = li.pop(1)
print(name)
name = li.pop() #默认删除一个
print(name)

print(li)

#remove 按元素删除
li.remove('alex')
#li.remove()  报错


# clear # 清空
print(li)

# del  默认全部
del li
print(li)

# del 
del li[2:]
print(li)


'''

#### 修改的方法
'''

#单个的修改
li[0]="太难了"
print(li)


#切片的修改
li[0:2] = "天真"
print(li)

li[0:2] = 'tianzhen'
print(li)

li[0:3] = [1,2,3,'天真','咸鱼']
print(li)

'''


#### 关于列表的一些方法
print(len(li))  #列表的长度

num = li.count('taibai')  #统计个数
print(num)
print(li.index("taibai"))  #所在的个数

#排序
'''
li1 =[4,1,2,5,3,6,9]
li2 =[4,1,2,5,3,6,9]
li1.sort()
li2.sort(reverse=True)
print(li2)
print(li1)
'''
##反转
# li1 =[4,1,2,5,3,6,9]
# li1.reverse()
# print(li1)

#列表的嵌套
# li = ['alex','wusir','egon',['alex','agon',58],25]
# print(li[1][1])
# print(li[1].capitalize())
# li[3][0]='bb'
# print(li)

###元祖  ->  只读列表，可循环查询，可切片
# 儿子不能改，孙子可能可以改
# tu = (1,2,3,'alex',[2,3,['taibai','bb']],'uu')
# print(tu)
#
# tu[4][2][1]='aa'
# print(tu)

#join 的方法

# s = 'alex'
# s1='_'.join(s)
# print(s1)
# print(''.join(s))

###列表 和字符串的相互转化
# # list-->str
# li=['aa','bb','cc']
# s=''.join(li)
# print(s)
# # str-->list
#
# s='aa_bb_cc'
# li1=s.split('_')
# print(li1)


### range

for i in range(2,10):
    print(i)

for i in range(2,10,2):
    print(i)

for i in range(10,2,-2):
    print(i)
