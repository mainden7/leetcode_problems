from collections import deque


class Tree:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

    def __repr__(self, level: int = 0):
        str_ = "   " * level
        str_ += f"Tree: {self.val}\n"
        for ch in self.children:
            str_ += ch.__repr__(level + 1)
        return str_

    def levels(self):
        lvl = {}

        def it(node, ll):
            lvl.setdefault(ll, []).append(node.val)
            for ch in node.children:
                it(ch, ll + 1)

        it(self, 0)
        return lvl

    def bfs(self, item):
        queue = deque()
        queue.appendleft(self)
        while queue:
            node = queue.popleft()
            if node.val == item:
                return item
            queue.extend(node.children)

    def breadth_paths(self):
        queue = list()
        queue.append((self, [self.val]))
        while queue:
            node, path = queue.pop(0)
            yield path
            for ch in node.children:
                queue.append((ch, path + [ch.val]))

    def bfs_paths(self, item):
        queue = list()
        queue.append((self, [self.val]))
        while queue:
            node, path = queue.pop(0)
            if node.val == item:
                return path
            for ch in node.children:
                queue.append((ch, path + [ch.val]))

    def dfs(self, search):
        if self.val == search:
            return search
        for ch in self.children:
            res = ch.dfs(search)
            if res != -1:
                return res
        return -1

    def depth_paths(self, path=None):
        if path is None:
            path = []
        path += [self.val]
        if not self.children:
            yield path
        for ch in self.children:
            yield from ch.depth_paths(path.copy())


class BinaryTree(Tree):
    def __init__(self, val, left=None, right=None):
        super().__init__(val)
        self.children = []
        self.left = left
        self.right = right
        if left:
            self.children.append(left)
        if right:
            self.children.append(right)

    def inorder(self):
        if self.left:
            yield from self.left.inorder()
        yield self.val
        if self.right:
            yield from self.right.inorder()

    def preorder(self):
        yield self.val
        if self.left:
            yield from self.left.preorder()
        if self.right:
            yield from self.right.preorder()

    def postorder(self):
        if self.left:
            yield from self.left.postorder()
        if self.right:
            yield from self.right.postorder()
        yield self.val

    def bfst(self):
        queue = deque()
        queue.appendleft(self)
        while queue:
            node = queue.popleft()
            yield node.val
            if node.children:
                queue.extend(node.children)

    @classmethod
    def from_list(cls, list_):
        # 2 * i + 1, 2 * i + 2
        for idx in range(len(list_)):
            if list_[idx] is None:
                list_.insert(2 * idx + 1, None)
                list_.insert(2 * idx + 2, None)

        def build(ls, i=0):
            if i >= len(ls) or ls[i] is None:
                return

            return BinaryTree(
                ls[i], left=build(ls, i * 2 + 1), right=build(ls, i * 2 + 2)
            )

        tree = build(list_)
        return tree


class BinarySearchTree(BinaryTree):
    @classmethod
    def from_list(cls, list_):
        if not list_:
            return
        mid = len(list_) // 2
        return cls(
            val=list_[mid],
            left=cls.from_list(list_[:mid]),
            right=cls.from_list(list_[mid + 1 :]),
        )

    @classmethod
    def from_unsorted_list(cls, list_, root=None):
        if not list_:
            return
        if root is None:
            root = cls(
                val=list_[0]
            )
        for val in list_[1:]:
            if val > root.val:
                if not root.left:
                    root = cls(val, left=root)
                else:
                    root.right = cls(val)
                    root = root.right
            else:
                if not root.right:
                    root = cls(val, right=root)
                else:
                    root.left = cls(val)
                    root = root.left
        return root





if __name__ == "__main__":

    # tr = BinarySearchTree.from_list([3, 5, 7, 10, 20, 30])
    tr = BinaryTree.from_list(sorted([3, 5, 1, 2, 7, 4, 6]))
    print(tr)
    # print(list(tr.inorder()))
    print(list(tr.preorder()))
    # print(list(tr.postorder()))
    # print(list(tr.bfst()))
    # print(list(tr.breadth_paths()))
    # print(list(tr.depth_paths()))
