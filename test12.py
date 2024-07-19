##
#本程序打印给定里氏震级的地震描述
#
#

#获取用户输入
richter=float(input("输入一个里氏地震震级："))

#打印地震描述
if richter>=8.0:#测试顺序错误
    print("绝大多数建筑倾覆")
elif richter>=7.0:
    print("许多建筑遭到损毁")
elif richter>=6.0:
    print("许多建筑开始遭到损伤，有一些会倒塌")
elif richter>=4.5:
    print("仅对建筑造成轻微损伤")
else:
    print("建筑无损害")
