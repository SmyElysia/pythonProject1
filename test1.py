#定义常量
PENNIES_PER_DOLLAR=100
PENNIES_PER_QUARTER=25

#从用户处获得输入
userInput=input("Enter bill value(1=$1 bill,5=$5 bill,etc.):")
billVaule=int(userInput)
userInput=input("Enter item price in pennies:")
itemPrice=int(userInput)

#计算找零金额
changeDue=PENNIES_PER_DOLLAR * billVaule -itemPrice
dollarCoins = changeDue//PENNIES_PER_DOLLAR
changeDue=changeDue%PENNIES_PER_DOLLAR
quarters=changeDue//PENNIES_PER_QUARTER

#打印找零金额
print("Dollar coins: %6d" % dollarCoins)
print("Quarters: %6d" % quarters)