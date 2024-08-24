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
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_child = left
        self.right_child = right


def search(target_value, node: TreeNode) -> TreeNode | None:
    if node is None or node.value == target_value:
        return node
    elif target_value > node.value:
        return search(target_value, node.right_child)
    else:
        # target_value < node.value:
        return search(target_value, node.left_child)


def insert(value, node: TreeNode) -> None:
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


def delete(value_to_delete, node: TreeNode):

    if node is None:
        return node

    elif value_to_delete < node.value:
        node.left_child = delete(value_to_delete, node.left_child)
        return node

    elif value_to_delete > node.value:
        node.right_child = delete(value_to_delete, node.right_child)
        return node

    elif node.value == value_to_delete:

        # returnしたnodeは、親nodeのleftもしくはright childになる。
        if node.left_child is None:
            return node.right_child
        elif node.right_child is None:
            return node.left_child
        else:
            node.right_child = lift(node.right_child, node)
            return node


def lift(node: TreeNode, nodeToDelete: TreeNode):
    if node.left_child:
        node.left_child = lift(node.left_child, nodeToDelete)
        return node
    else:
        nodeToDelete.value = node.value
        return node.right_child


def traverse_and_print(node: TreeNode):
    """
    ツリーの要素をvalueが小さいものから順に出力
    """
    if node is None:
        return
    traverse_and_print(node.left_child)
    print(node.value)
    traverse_and_print(node.right_child)


root = TreeNode(value=10)
root.left_child = TreeNode(5)
root.right_child = TreeNode(20)

# delete(5, root)
traverse_and_print(root)
