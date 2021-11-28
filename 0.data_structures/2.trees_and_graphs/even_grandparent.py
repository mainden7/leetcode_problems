class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self, lvl=0):
        s = " " * lvl
        s += f"TreeNode: {self.val}\n"
        for ch in [self.left, self.right]:
            if ch:
                s += ch.__repr__(lvl + 1)
        return s


def sum_even_grandparent(root):
    ans = []

    def dfs(node, parent=None, gp=None):
        if not node:
            return

        if gp is not None and gp.val % 2 == 0 and node.val:
            ans.append(node.val)
        dfs(node.left, parent=node, gp=parent)
        dfs(node.right, parent=node, gp=parent)

    dfs(root)
    return sum(ans)


def from_list(list_, idx=0):
    if idx >= len(list_):
        return
    node = TreeNode(list_[idx])
    node.left = from_list(list_, idx=(2 * idx + 1))
    node.right = from_list(list_, idx=(2 * idx + 2))
    return node


if __name__ == "__main__":
    # tree = from_list([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])
    tree = from_list([6, 1, 2])
    print(sum_even_grandparent(tree))
