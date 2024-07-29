##
# 本程序使用Python中的海龟图形包绘制一条希尔伯特曲线
#
import turtle

def main():
    turtle.reset()
    turtle.penup()
    n =6
    turtle.goto(-n ** 2 * 10 / 2,n ** 2 * 10 / 2)
    turtle.pendown()
    hilbert(n,90,10)
    response= input ("Press ENTER to quit.")

# 使用海龟图形包绘制第n代希尔伯特曲线
# @param n 一个表示第n代曲线的整数
# @param turn 海龟旋转的角度
# @param distance 海龟向前移动的距离（像素数）
#
def hilbert(n,turn,distance):
    if n==1:
        turtle.forward(distance)
        turtle.right(turn)
        turtle.forward(distance)
        turtle.right(turn)
        turtle.forward(distance)
        # 或者，使用更优雅的方式
        # turtle.right(2*turn)
    else:
        turtle.right(turn)
        hilbert(n-1,-turn,distance)
        turtle.right(turn)
        turtle.forward(distance)
        hilbert(n-1,turn,distance)
        turtle.left(turn)
        turtle.forward(distance)
        turtle.left(turn)
        hilbert(n-1,turn,distance)
        turtle.forward(distance)
        turtle.right(turn)
        hilbert(n-1,turn,distance)
        turtle.right(turn)

main()