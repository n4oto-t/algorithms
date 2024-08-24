"""
accessとdeletionはクラシックなQueue同様、先頭から処理を行う。しかし、insertionは特定の順序を保つよう工夫される。

病院の患者の列のイメージ。
風邪の患者A,B,Cが3人待ってるときに、交通事故患者が運ばれたらQueueの先頭にinsertされる。

before:[A , B , C]
after :[D , A , B , C]
        first <--  last
"""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self._next_node = None

    @property
    def next_node(self) -> "Node":
        return self._next_node

    @next_node.setter
    def next_node(self, node: "Node"):
        self._next_node = node


class Priority_Queue:
    def __init__(self, first_node: Node | None = None) -> None:
        self.first_node = first_node

    def insert_data_into_queue(self, data: int):
        new_node = Node(data)

        # queueが空のとき
        if self.first_node is None:
            self.first_node = new_node
            return

        # queueの先頭に追加するケース
        if data > self.first_node.data:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return

        current_node = self.first_node
        next_node = current_node.next_node
        while next_node is not None:
            if current_node.data < data < next_node.data:
                new_node.next_node = next_node
                current_node.next_node = new_node
                return
            current_node = next_node
            next_node = next_node.next_node

        # queueの最後に追加するケース
        current_node.next_node = new_node
