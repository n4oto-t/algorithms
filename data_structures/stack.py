"""
LIFO
"""


class Stack:
    def __init__(self) -> None:
        self.stack: list = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            print("stackにアイテムなし")

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def __repr__(self) -> str:
        return "\n".join(str(i) for i in self.stack)
