

### 五、计算用户输入的内容中有几个整数。    #hskj545dsf548w554g6
count = input(">>>")
for i in count:
    if i.isalpha() :
        count=count.replace(i," ")

print(count)
l=count.split()
print(l)
print("整数的个数："+str(len(l)))

