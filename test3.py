from ezgraphics import GraphicsWindow
win=GraphicsWindow(500,500)
canvas=win.canvas()
canvas.drawRect(15,10,20,30)
win.wait()#等待用户关闭窗口
