##
# 本程序处理一幅数字图像
# 生成原始图像的负片
#

from ezgraphics import GraphicsImage, GraphicsWindow

filename = input("Enter the name of the image file: ")

# 从文件中载入图像
image = GraphicsImage(filename)

# 处理图像
width = image.width
height = image.height()
for row in range(height):
    for col in range(width):
        # 获取当前像素
        red = image.getRed(row,col)
        green = image.getGreen(row,col)
        blue = image.getBlue(row,col)

        # 过滤像素
        newRed = 255 - red
        newGreen = 255 - green
        newBlue = 255 - blue

        # 设置像素为新颜色
        image.setPixel(row, col, newRed, newGreen, newBlue)

# 在屏幕上显示图像
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(image)
win.wait()

# 把新图像保存为一个新文件
image.save("negative-"+filename)