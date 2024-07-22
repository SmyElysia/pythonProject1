##
# 绘制一个目标靶
# 由用户指定圆环的数量
#

from ezgraphics import GraphicsWindow

# 定义常量
MIN_NUM_RINGS = 2
MAX_NUM_RINGS = 10
RING_WIDTH = 25
TARGET_OFFSET = 10

# 读取目标靶中圆环的数量
numRings = int(input("Enter # of rings  in the target:"))
while numRings < MIN_NUM_RINGS or numRings > MAX_NUM_RINGS:
    print("Error: the number of rings must be between",
          MIN_NUM_RINGS,"and",MAX_NUM_RINGS)
    numRings = int(input("Re-enter # of rings  in the target:"))

# 确定最外面圆的直径，将首先绘制最外面的圆
diameter = (numRings+1) * RING_WIDTH * 2

# 根据最外面圆的大小确定窗口的尺寸
winSize = diameter + 2 * TARGET_OFFSET

# 创建图形窗口对象，并获取画布对象
win = GraphicsWindow(winSize,winSize)
canvas = win.canvas()

# 设置画布的背景色为浅灰色
canvas.setBackground('light grey')

# 绘制圆环，交替使用黑色和白色来填充
x = TARGET_OFFSET
y = TARGET_OFFSET
for ring in range(numRings):
    if ring % 2 ==0:
        canvas.setColor("black")
    else:
        canvas.setColor("white")
    canvas.drawOval(x,y,diameter,diameter)

    diameter=diameter -2 * RING_WIDTH
    x=x+RING_WIDTH
    y=y+RING_WIDTH

    # 使用红色绘制靶心
    canvas.setColor("red")
    canvas.drawOval(x,y,diameter,diameter)

    win.wait()