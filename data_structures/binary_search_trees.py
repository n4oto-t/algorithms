"""
要素をあらかじめソートした状態でデータを持ち、挿入・削除・検索を少ない計算量で実行できるデータ構造

Binary tree
各nodeが最大で2つの子ノードを持つ

Binary search tree
Binary Treeの一種で、各ノードに以下の条件が適用される:
左の子ノード（left child）の値は、親ノードの値より小さい。
右の子ノード（right child）の値は、親ノードの値より大きい。
"""


class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left_child = left
        self.right_child = right


def search(target_value, node: TreeNode) -> TreeNode:
    if node is None or node.value == target_value:
        return node
    elif target_value > node.value:
        return search(target_value, node.right_child)
    elif target_value < node.value:
        return search(target_value, node.left_child)


def insert(value, node: TreeNode):
    if value > node.value:
        if node.right_child is None:
            node.right_child = TreeNode(value)
        else:
            insert(value, node.right_child)

    elif value < node.value:
        if node.left_child is None:
            node.left_child = TreeNode(value)
        else:
            insert(value, node.left_child)
