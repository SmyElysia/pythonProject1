##
#本程序在画布上绘制三个矩形
#

from ezgraphics import GraphicsWindow

#创建窗口并访问画布
win= GraphicsWindow(400,200)
canvas = win.canvas()

#在画布上绘图
canvas.drawRect(0,10,200,10)
canvas.drawRect(0,30,300,10)
canvas.drawRect(0,50,100,10)

#等待用户关闭窗口
win.wait()