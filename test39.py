## 创建一个条形图
# 显示一个量经过多年的累加增长或者衰减的情况
# @param initial (float) 量的初始值
# @param rate (float)
# @param years (int) 图表中显示的年数
# @param bardistance(int) 相邻两个条形之间相隔的年数
# @param title (string) 图表的标题
#
import matplotlib as pyplot
def showGrowthChart(initial,rate,years,bardistance,title):

    amount=initial
    bar=0

    # 绘制初始数量的条形图
    pyplot.bar(bar,amount,align="center")
    bar = bar + 1
    year =1
    while year <=years:
        change = amount * rate /100
        amount = amount + change
        # 如果应该在当前年份绘制条形图，则绘制一个条形图
        if year % bardistance == 0:
            pyplot.bar(bar,amount,align="center")
            bar = bar + 1
        year = year + 1

    if rate >=0:
        subtitle = "Growth rate %.4f percent" % rate
    else:
        subtitle = "Decay rate %.4f percent" % -rate

    pyplot.title(title+"\n"+subtitle)

    # 配置坐标轴
    pyplot.xlabel("Year")
    pyplot.ylabel("Amount")
    pyplot.xticks(range(0,bar),range(0,year,bardistance))

    # 调整绘图区域以紧密围绕条形图
    pyplot.xlim(-0.5,bar,-0.5)

    pyplot.show()


    # 测试函数
    def main():
        showGrowthChart(1000.0,1.0,500,50,"Bank balance")
        showGrowthChart(100.0,-0.0121,6000,500,"Carbon decay")