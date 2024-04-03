"""
リストを、要素が一つになるまで半分ずつに分けていく。
リストAとBの要素を比較し、小さいほうをresultに追加する。
計算量 O(n logn)

[3,1,9,4,2]
[3,1] , [9,4,2]
[3] , [1] , [9] , [4,2]
[3] , [1] , [9] , [4] , [2] 
[1,3] , [4,9] ,[2]
[1,3] , [2,4,9]
[1,2,3,4,9]
"""


def merge_sort(ary: list[int]):
    if len(ary) == 1:
        return ary

    mid = len(ary) // 2
    left = merge_sort(ary[:mid])
    right = merge_sort(ary[mid:])

    return merge(left, right)


def merge(left: list, right: list):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # left , rightいずれかの要素を全てresultにappendしたらwhileを抜けてしまう。ここの処理で、left , rightいずれかに残っている要素をresultへ追加する。
    result += left[i:]
    result += right[j:]
    return result


# このデータの場合、まずmerge_sortによって、left=[5] , right=[4,2]が定義される。再帰的にright[4,2]を引数にとってmerge_sortが実行される。要素数が1ではないため、mergeメソッドまで実行される。結果的にleft=[5] , right=[2,4]となり、次はこの二つの配列に対してmergeメソッドが実行される。
ary = [5, 4, 2]
sorted_arr = merge_sort(ary)
print("Sorted array is:", sorted_arr)
