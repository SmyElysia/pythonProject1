string=input("请输入一个字符串：")
position=len(string)//2
if len(string)%2==1:
    result=string[position]
else:
    result=string[position-1]+string[position]
print(result)