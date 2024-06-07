from decimal import Decimal

def is_equal_ignore_point_and_sign(one: Decimal, other: Decimal) -> bool:
    """
    忽略小数点位数及正负号 比较两个数是否相等
    """
    one, other = abs(one), abs(other)
    return one == other or (one * 10**len(str(one)) == other * 10**len(str(other)))



if __name__ == "__main__":
    print(is_equal_ignore_point_and_sign(Decimal("0.1"), Decimal("0.10"))) # True
    print(is_equal_ignore_point_and_sign(Decimal("0.1"), Decimal("0.11"))) # False
    print(is_equal_ignore_point_and_sign(Decimal("-0.1"), Decimal("-0.10"))) # True
    print(is_equal_ignore_point_and_sign(Decimal("-0.1"), Decimal("-0.11"))) # False
    print(str(2.300))
    print(str(230.0))