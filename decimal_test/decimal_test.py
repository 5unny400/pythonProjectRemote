from decimal import Decimal, getcontext

# 设置精度为小数点后六位
getcontext().prec = 8  # 总位数为 8，小数点后六位

# 使用 Decimal 类来进行精确运算
number1 = Decimal('3.141592')
number2 = Decimal('2.718281')


result = number1 + number2

print("Decimal:"+str(result))

number3 = Decimal('1.5')
number4 = 1.5

plus_num3 = Decimal('1.3')
plus_num4 = 1.3

print("Decimal:"+str(number3+plus_num3))
print("not Decimal:"+str(number4+plus_num4))