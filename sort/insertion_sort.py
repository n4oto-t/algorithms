"""
worst scenario
比較： (N^2)/2
入れ替え：(N^2)/2
remove:N-1
insert:N-1
sum = N^2 + 2N -2
計算量O(N^2)
"""


def insertion_sort(ary: list[int]):

    for i in range(1, len(ary)):
        position = i - 1  # positonはtmp_valueの一個左のインデックス。
        tmp_value = ary[i]  # 比較の基準となる値

        while position >= 0:
            if ary[position] > tmp_value:
                ary[position + 1] = ary[position]
                position -= 1
            else:
                break
        ary[position + 1] = tmp_value
    return ary


print(insertion_sort([3, 5, 2, 7]))
