"""
スマホのauto complete機能を実装することができる構造
"""


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode | None] = {}


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def search(self, word: str):
        current_node = self.root

        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                return None
        return current_node

    def insert(self, word: str):
        current_node = self.root
        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                new_node = TrieNode()
                current_node.children[char] = new_node

                current_node = new_node
        current_node.children["*"] = None

    def collect_all_words(
        self, node: TrieNode | None = None, word: str = "", words: list[str] = []
    ):
        current_node = node or self.root

        for key, child_node in current_node.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collect_all_words(child_node, word + key, words)
        return words

    def auto_complete(self, prefix: str):
        current_node = self.search(prefix)
        if not current_node:
            return None
        return self.collect_all_words(current_node)
