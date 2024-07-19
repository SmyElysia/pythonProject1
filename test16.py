##
# 本程序模拟跳过13楼的电梯控制面板
# 并检测输入错误
#

#通过用户输入获取楼层号（整数）
floor =int(input("楼层："))

#确保用户输入的正确性
if floor ==13:
    print("错误：没有第十三层！")
elif floor<=0 or floor>20:
    print("错误：楼层必须在1至20层之间！")
else:

#此处可以确定输入有效
    actualFloor=floor
    if floor>13:
        actualFloor=floor-1

    print("电梯将前往实际楼层……")