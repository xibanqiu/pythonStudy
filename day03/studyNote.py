i = 100
print(i.bit_length())  #7

''''
数字     二进制       bit_length值
1        0000 0001     1
2        0000 0010     2
3        0000 0011     2
'''

#int  ---> str
i = 1
s =str(i)

#str ---> int
s = '123'
i = int(s)

#int --> bool  只要是0 ---》False 非0就是 True
i=3
b=bool(i)
print(b)  #True

# >bool  ---> int
# True == 1
#False -- 0

'''
ps：
while True :
    ...
while 1 ; 效率高
    ...

'''


# str --> bool

s = ""
print(bool(s))  #False

s = "0"
print(bool(s))  #True


print(str(True))