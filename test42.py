##
# 本程序使用Python的海龟图形包
# 绘制一个正方形和一条垂直线
#
import turtle

# 使用默认颜色和画笔绘制一个正方形
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

# 在正方形框的右侧绘制一条红色的垂直粗线
turtle.pensize(3)
turtle.pencolor('red')
turtle.penup()
turtle.forward(90)
turtle.forward(200)
turtle.right(90)
turtle.pendown()
turtle.forward(100)

# 等待用户输入，然后退出程序
response = input("Press ENTER to quit.")