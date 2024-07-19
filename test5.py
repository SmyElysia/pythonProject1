#
#本程序在画布上绘制三个有颜色填充的矩形
from ezgraphics import GraphicsWindow
win=GraphicsWindow(400,200)
canvas=win.canvas()

canvas.setColor("red")
canvas.drawRect(0,10,200,10)

canvas.setColor("green")
canvas.drawRect(0,30,300,10)

canvas.setColor("blue")
canvas.drawRect(0,50,300,10)

#等待用户关闭窗口
win.wait()

