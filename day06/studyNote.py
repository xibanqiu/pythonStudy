

#python2 和 python3 的一些区别
'''

#python2
print('aaa') print'aaa'
range() xrange()生成器
raw_input()


#python3
print('aaa')
range()
#input()

'''

# = 赋值  == 比较值是否相等  is 比较的是内存地址  id(内容)-->可以看到内存地址
li1 = [1,2,3]
li2=li1
li3 =li2
print(li1 is li2)
print(li1 == li2)
print(id(li1),id(li2))

# 数字 字符串 有一个小数据池的概念即在这个范围内的数据的地址一样
#数字的范围 -5到256
#字符串 没有具体的定义：有一些规律：1、不能有特殊的字符
                                # 2、（单个字母例如：s）s*20 还是同一个地址，s*21以后都是两个地址

'''
i1 = 6
i2 = 6
print(id(i1),id(i2))
i3 = 600
i4 = 600
print(i3 is i4)
print(id(i3),id(i4))

#剩下的 list dict tuple set 地址值都不会相等
li1=[1,]
li2=[1,]
print(li1 is li2)
'''

#编码
'''
ascii       A : 00000010                                  8位   1个字节
unicode     A : 00000000 00000000 00000000 00000110       32位   4个字节
            中：00000000 00000000 00000110 00000110       32位   4个字节
utf_8       A:00000110                                    8位   1个字节
            中：00000000  00000110 00000110               24位   3个字节
GBK          A:00000110                                    8位   1个字节
            中：00000000   00010110                        16位   2个字节
            
 总结：           
1、各个编码之间的二进制，是不能互相识别的，会产生乱码。
2、文件的存储，传输，不能是unicode （只能是 utf-8,utf-16  gbk  gb2312 ascii 等）
'''

# bytes 类型
'''
#python 3 :str 在内存中是以 unicode编码存储的。
        对于英文：str :表现的形式 : s='alex'
                       编码方式：010101010     unicode
                  bytes: 表现的形式 : s=b'alex'
                        编码方式：010101010     utf-8 、 gbk
        对于中文：str :表现的形式 : s='中国'
                       编码方式：010101010     unicode
                  bytes: 表现的形式 : s=b'\e91\e95\e93\e91'   -->gbk
                        编码方式：010101010     utf-8 、 gbk
                        
s = 'alex'
s1 = b'alex'
print(s,type(s))  #alex <class 'str'>
print(s,type(s1))   #alex <class 'bytes'>

#encode 编码 ,将str-->bytes
sl1=s.encode('utf-8')
print(sl1)  #b'alex'

s2 = '中国'
s22 = s2.encode("utf-8")
print(s22)  #b'\xe4\xb8\xad\xe5\x9b\xbd'
'''

