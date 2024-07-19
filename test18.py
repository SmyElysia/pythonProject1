##
# 本程序演示使用matplotlib模块绘制条形图的步骤
#
#

from matplotlib import pyplot as plt

# 在图表上绘制数据
plt.bar(1,1.1)
plt.bar(2,10.0)
plt.bar(3,25.4)
plt.bar(4,44.5)
plt.bar(5,61.0)

# 添加描述信息
plt.xlabel("Month")
plt.ylabel("Temperature")

# 显示图表
plt.show()