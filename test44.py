##
# 本程序读取一系列值，然后打印这些值，并标记出最大值
#
#

# 创建一个空列表
values = []

# 读取输入值
print("Please enter values,Q to quit:")
userInput = input("")
while userInput.upper() !="Q":
    values.append(float(userInput))
    userInput = input("")

# 查找最大值
largest = values[0]
for i in range(1,len(values)):
    if values[i] > largest:
        largest = values[i]

# 打印所有的值，并标记最大值
for element in values:
    print(element,end="")
    if element == largest:
        print(" <== largest value",end="")
    print()