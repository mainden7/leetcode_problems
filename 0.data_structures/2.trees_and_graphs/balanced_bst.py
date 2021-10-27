class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self, lvl=0, ss=""):
        s = "  " * lvl
        s += f"{ss}Tree: {self.val}\n"
        if self.left:
            s += self.left.__repr__(lvl + 1, "(l)")
        if self.right:
            s += self.right.__repr__(lvl + 1, "(r)")
        return s

    @classmethod
    def make_balanced(cls, arr):
        if not arr:
            return

        n = len(arr)
        mid = n // 2
        left = arr[:mid]
        right = arr[mid + 1 :]

        root = TreeNode(
            val=arr[mid],
            left=cls.make_balanced(left),
            right=cls.make_balanced(right),
        )
        return root

    def rotate_left(self):
        pass

    def rotate_right(self):
        root = self.left
        self.left = root.right
        root.right = self
        return root



if __name__ == "__main__":
    aa = TreeNode.make_balanced([-1, 2, 3, 4, 5, 7])
    print(aa)
    # bb = aa.rotate_left()
    cc = aa.rotate_right()
    print(cc)

    # print(aa)
