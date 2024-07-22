##
# 本程序通过模拟投掷飞镖到一个
# 正方形靶标上来计算Π的估计值
#

from random import random

TRIES = 10000

hits = 0
for i in range(TRIES):

    # 生成两个位于-1~1的随机数
    r = random()
    x = -1 + 2 * r
    r = random()
    y = -1 + 2 * r

    # 检查该点是否位于单位圆之内
    if x * x+y * y <=1 :
        hits += 1
# 命中次数/投射次数的比值近似于
# 圆的面积/正方形的面积 = pi / 4

piEstimate = 4.0 * hits / TRIES
print('Estimated for pi :%.4f', piEstimate)