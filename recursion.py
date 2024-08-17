"""
Question:N段ある階段の登り方は何通りあるか。

一回のアクションによって登れる階段の数は3通り。
1. 1段のぼる
2. 2段のぼる
3. 3段のぼる

N段目へ到達する方法は以下の3通り。
1. N-3段目から3段のぼる
2. N-2段目から1段登りと、2段上りの組み合わせ。
3. N-1段目から1段のぼる。


0段の階段の登り方が1通りである理由
0段目にすでに「いる」状態を「1通り」とカウントするため。つまり、0段目に到達するための方法は何も行動しないという1通りの方法があると考える。

"""


def number_of_paths(n):
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1
    if n == 2:
        return 2

    return number_of_paths(n - 3) + number_of_paths(n - 2) + number_of_paths(n - 1)


print(number_of_paths(3))


def anagram_of(string):
    if len(string) == 1:
        return [string]

    collection = []
    substring_anagrams = anagram_of(string[1:])

    for substring_anagram in substring_anagrams:
        for index in range(len(substring_anagram) + 1):
            # 文字列のコピーを作成し、文字を挿入
            copy = substring_anagram[:index] + string[0] + substring_anagram[index:]
            collection.append(copy)

    return collection


print(anagram_of("abc"))
