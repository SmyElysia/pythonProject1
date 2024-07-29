##
# 本程序创建包含正弦三角函数和余弦三角函数的图形
# x坐标的范围为-180°~180°
#

from matplotlib import pyplot as plt
from math import pi,sin,cos

# 创建两个空列表，用于保存正弦函数和余弦函数的y坐标值
sinY = []
cosY = []

# 两条曲线的x坐标相同
trigX = []

# 计算正弦函数和余弦函数的y坐标
angle = -180
while angle <= 180 :
    x = pi / 180 * angle
    trigX.append(x)

    y=sin(x)
    sinY.append(y)

    y=cos(x)
    cosY.append(y)
    angle = angle + 1

# 绘制两条曲线
plt.plot(trigX,sinY)
plt.plot(trigX,cosY)

# 添加描述信息
plt.title("Trigonometric Functions")

# 改善图表的外观
plt.legend(["sin(x)","cos(x)"])
plt.grid('on')
plt.axis('equal')
plt.axvline(color='k')
plt.axvline(color="k")

plt.show()