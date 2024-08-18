class Node:
    def __init__(self, data) -> None:
        self.data = data
        self._next_node = None

    @property
    def next_node(self) -> "Node":
        return self._next_node

    @next_node.setter
    def next_node(self, node: "Node"):
        self._next_node = node


class LinkedList:
    def __init__(self, first_node: Node) -> None:
        self.first_node = first_node

    def read(self, index: int) -> str | None:
        current_node = self.first_node
        current_index = 0

        while current_index < index:
            current_node = current_node.next_node
            current_index += 1

            if current_node is None:
                return None
        return current_node.data

    def index_of(self, target_value: str) -> int | None:
        current_node = self.first_node
        current_index = 0

        while current_node is not None:
            if current_node.data == target_value:
                return current_index

            current_node = current_node.next_node
            current_index += 1

        return None

    def insert_at_index(self, index: int, value) -> None:
        new_node = Node(value)
        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return

        current_index = 0
        current_node = self.first_node

        while current_index != index - 1:
            current_index += 1
            if current_node.next_node is None:
                return
            current_node = current_node.next_node

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def delete_at_index(self, index: int) -> None:
        if index == 0:
            self.first_node = self.first_node.next_node
            return

        current_node = self.first_node
        current_index = 0
        while current_index != index - 1:
            current_index += 1
            if current_node.next_node is None:
                return
            current_node = current_node.next_node

        current_node.next_node = current_node.next_node.next_node


node1 = Node("once")
node2 = Node("upon")
node3 = Node("a")
node4 = Node("time")

node1.next_node = node2
node2.next_node = node3
node3.next_node = node4

linked_list = LinkedList(node1)
# print(linked_list.read(2))

# linked_list.index_of("aaaaaa")
print(linked_list.read(0))
linked_list.insert_at_index(0, "hoge")
print(linked_list.read(0))


"""
next_nodeだけでなく、previous_nodeへのポインタを持つDoubly linked Listsがある。
リストの最初、最後への要素の追加・削除がO(1)になるため、Queueに適している。arrayでQueueを実装した場合、最後の要素を削除するのにO(N)要する。
"""
