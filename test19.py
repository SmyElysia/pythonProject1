##
# 本程序创建一个简单的折线图，通过本程序演示了matplotlib模块的许多功能
#

from matplotlib import pyplot

# 在图表上绘制数据
pyplot.plot([1,2,3,4,5,6,7,8,9,10,11,12],[1.1,10.0,25.4,44.5,61.0,71.6,72.7,65.9,54.6,31.9,10.9,4.8])
pyplot.plot([1,2,3,4,5,6,7,8,9,10,11,12],[-16.9,-12.7,-2.5,20.6,37.8,49.3,52.3,46.4,35.1,16.5,-5.7,-12.9])

# 修改x的范围，增加填充空白
pyplot.xlim(0.8,12.2)

# 添加描述性信息
pyplot.title("Average Temperatures in Fairbanks")
pyplot.ylabel("Temperature (F)")
pyplot.legend(["High","Low"])

pyplot.xticks(
    [1,2,3,4,5,6,7,8,9,10,11,12],
    ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
)

# 显示图表
pyplot.show()