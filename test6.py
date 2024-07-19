##
#本程序使用ezgraphics模块绘制一面意大利旗帜
#

from ezgraphics import GraphicsWindow

win=GraphicsWindow(300,300)
canvas=win.canvas()

#使用左上角位置和大小定义变量
xLeft=100
yTop=100
width=90

#绘制旗帜
canvas.setColor("green")
canvas.drawRect(xLeft,yTop,width/3,width*2/3)

canvas.setColor("red")
canvas.drawRect(xLeft+2*width/3,yTop,width/3,width*2/3)

canvas.setColor("black")
canvas.drawLine(xLeft+width/3,yTop+width*2/3,xLeft+width*2/3,yTop+width*2/3)

#等待用户关闭窗口
win.wait()