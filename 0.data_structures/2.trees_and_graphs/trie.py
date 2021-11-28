import json


class Trie:
    __slots__ = ("root", "counter")

    def __init__(self):
        self.root = {}
        self.counter = 0

    def __repr__(self) -> str:
        return json.dumps(self.root, indent=2)

    def __len__(self):
        return self.counter

    def __contains__(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return "_end_" in node

    def insert(self, *words: str) -> None:
        for word in words:
            node = self.root
            for letter in word:
                node = node.setdefault(letter, {})
            node["_end_"] = "_end_"
            self.counter += 1

    def delete(self, word: str) -> None:
        if not self.root:
            raise ValueError
        node = self.root
        for letter in word:
            node = node.get(letter)
            if not node:
                break
        else:
            del node["_end_"]


if __name__ == "__main__":
    trie = Trie()
    trie.insert("abc", "cda")
    print(trie)
    trie.delete("abc")
    print(trie)
    # print("abcc" in trie)
    # trie.insert("abcc")
    # print("abcc" in trie)
    # trie.delete("abcc")
    # print(trie)
    # print("abcc" in trie)
