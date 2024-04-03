"""
配列の中から最小値を見つけ出し、その値を先頭に移動させる処理を繰り返し行う。
計算量 O(N**2)
"""


def selection_sort(ary: list):
    N = len(ary)
    for i in range(N - 1):  ##最後の要素に対する比較は不要なため、N-1としている。
        index_of_min = i  ##最小値のインデックス番号を仮置き
        for j in range(i + 1, N):
            if ary[index_of_min] > ary[j]:
                index_of_min = j
        tmp = ary[i]
        ary[i] = ary[index_of_min]
        ary[index_of_min] = tmp

    return ary


print(selection_sort([3, 2, 5, 6, 22, 1]))
