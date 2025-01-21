"""
2分探索
要素がソートされていることが前提。


要素数がNのとき、1回の探索で対象範囲を半分に減らすことできる。これを繰り返すことで、探索対象は次のように減少する
N -> N/2 -> N/4 -> ... -> 1となる。

探索範囲が1になるまでの回数をkとすると、2^k = N となるとき探索が完了する。
対数の形にすると k = log2(N)なので、計算量はlog(N)。

"""

target = 41
ary = [2, 4, 5, 7, 11, 14]


def binary_search(ary, target):
    left = 0
    right = len(ary) - 1

    while left <= right:
        center = (left + right) // 2
        value_of_center = ary[center]

        if target == ary[center]:
            return True

        if target < value_of_center:
            right = center - 1
        elif target > value_of_center:
            left = center + 1

    return False


print(binary_search(ary, target))
