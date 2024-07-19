##
# 本程序模拟一个跳过13楼的电梯控制面板

#根据用户输入获取楼层号（整数）
floor=int(input("楼层："))

#如果需要，调整楼层
if floor>13:
    actualFloor=floor-1
else:
    actualFloor=floor

#打印结果
print("电梯将去往实际楼层：",actualFloor)