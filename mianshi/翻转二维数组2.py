

def test(list1):
    x = len(list1)
    y = len(list1[0])

    # 声明新的list，新的list的行列长度和list1的刚好互换
    new_list = [[0 for _ in range(x)] for _ in range(y)]

    for i in range(x):
        for j in range(y):
            new_list[j][i] = list1[i][j]

    print(new_list)



list1 = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 10],
]
test(list1)