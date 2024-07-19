##本程序用于计算运输费用
#
#

#获取用户输入
country=input("Enter the country:")
state=input("Enter the state or province:")

#计算运输费用
shippingCost=0.0

if country=="USA":
    if state=="AK" or state=="HI":
        shippingCost=10.0
    else:
        shippingCost=5.0
else:
    shippingCost=10.0

#打印结果
print("Shipping cost to %s,%s:$%.2f"%(state,country,shippingCost))
