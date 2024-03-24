"""
1. 基準値を一つ選び、基準値より値が小さいリスト、大きいリストの2つに分割する。
2. 小さいリスト、大きいリストそれそれに対して再帰的に処理を行なってソートしていく。

平均的にO(n logn)の計算量。

"""


def quick_sort(ary: list[int]) -> list[int]:
    if len(ary) < 2:
        return ary

    ##適当な数値としてaryの真ん中の要素を選択。
    pivot = ary[len(ary) // 2]

    lower, same, greater = [], [], []

    for i in ary:
        if i == pivot:
            same.append(i)
        elif i > pivot:
            greater.append(i)
        elif i < pivot:
            lower.append(i)
    return quick_sort(lower) + same + quick_sort(greater)


ary = [3, 5, 43223, 42, 52, 64356, 45, 1]
print(quick_sort(ary))
