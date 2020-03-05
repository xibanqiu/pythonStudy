
### 只读
# f= open ("models",mode="r",encoding="utf-8")   # 第一个参数为 文件路径：分为相对路径和绝对路径，这里为相对路径;第二个为对文件袋的操作方式，第三个为编码
# content = f.read();
# print(content)
# f.close() #关闭流

# 以bytes 的形式 只读
# f= open( "models",'rb',)
# content =f.read()
# print(content)
# f.close()

### 只写 ,会先将文件的内容全部清除后，在写
# f=open("models",'w',encoding="utf-8")
# f.write("你过来呀w")
# f.close()
#
# f=open("models",'wb',)
# f.write("你过来呀wb".encode('utf-8'))
# f.close()

### 追加
# f = open("models",'a',encoding="utf-8")
# f.write("琪亚娜")
# f.close();

# f = open("models",'ab')
# f.write("琪亚娜".encode('utf-8'))
# f.close();

