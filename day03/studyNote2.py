s = 'ABCDLSESRF'

# 索引
s1 = s[0]
print(s1)             #A

s2 = s[-1]
print(s2)             #F

#得到ABCD 切片：顾头不顾尾
s3 = s[0:4]
print(s3)     #ABCD

s6 = s[0:-1]
print(s6)   #ABCDLSESR

s7 = s[:]
print(s7)  #ABCDLSESRF
s8 = s[0:]
print(s8) #ABCDLSESRF

s9 =s[0:0]
print(s9)  #空的字符串
s10=s[0:5:2]
print(s10) #ACL

s11 = s[4::-1]
print(s11)  #LDCB
s12=s[3::-1]
print(s12) #DCBA