##
#绘制两个圆，并确定它们是否相交
#通过用户输入获取两个圆的参数
#

from ezgraphics import GraphicsWindow
from math import sqrt
from sys import exit

#定义常量变量
MIN_RADIUS=5
WIN_WIDTH=500
WIN_HEIGHT=500

#创建图形窗口对象，并获取画布对象
win=GraphicsWindow(WIN_WIDTH, WIN_HEIGHT)
canvas=win.canvas()

#获取第一个圆的参数
print("请输入第一个圆的参数：")
x0=int(input("x坐标："))
y0=int(input("y坐标："))
if x0<0 or x0>= WIN_WIDTH or y0<0 or y0 >= WIN_HEIGHT:
    exit("错误：圆心必须在窗口区域范围内！")

r0=int(input("半径："))
if r0<=MIN_RADIUS:
    exit("错误：半径必须大于",MIN_RADIUS)

#绘制第一个圆
canvas.setOutline("blue")
canvas.drawOval(x0-r0,y0-r0,2*r0,2*r0)

#获取第二个圆的参数
print("请输入第二个圆的参数：")
x1=int(input("x坐标："))
y1=int(input("y坐标："))
if x1<0 or x1>= WIN_WIDTH or y1<0 or y1 >= WIN_HEIGHT:
    exit("错误：圆心必须在窗口区域范围内！")

r1=int(input("半径："))
if r1<=MIN_RADIUS:
    exit("错误：半径必须大于",MIN_RADIUS)

# 绘制第二个圆
canvas.setOutline("red")
canvas.drawOval(x1 - r1, y1 - r1, 2 * r1, 2 * r1)

#确定两个圆是否相交，并选择相应提示信息
dist=sqrt((x1-x0)**2+(y1-y0)**2)

if dist>r0+r1:
    message="两个圆完全分离"
elif dist<abs(r0-r1):
    message="一个圆包含另一个圆"
elif dist==r0+r1:
    message="两圆有一个交点"
elif dist==0 and r0==r1:
    message="两个圆重合"
else:
    message="两个圆有两个交点"

#在图形窗口的底部向上显示结果信息
canvas.setOutline("black")
canvas.drawText(15,WIN_HEIGHT-15,message)

#等待，直到用户关闭窗口
win.wait()