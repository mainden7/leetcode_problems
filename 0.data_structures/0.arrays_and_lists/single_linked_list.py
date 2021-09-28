class SingleLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None

        if nodes:
            data = nodes.pop(0)
            node = Node(data)
            self.head = node

            while nodes:
                data = nodes.pop(0)
                next_node = Node(data)
                node.next = next_node
                if not self.tail and not nodes:
                    self.tail = next_node

                node = next_node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        return "->".join([str(n.val) for n in self.__iter__()])

    def insert(self, node):
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def append(self, node):
        self.tail.next = node
        self.tail = node

    def delete(self, val):
        for n in self:
            if n.next.val == val:
                n.next = n.next.next
                break

    def distinct(self):
	# simple approach
        nodes = set()
        for node in self:
            nodes.add(node.val)
        return SingleLinkedList(list(nodes))

    def remove_duplicates(self):
	# better approach than self.distinct
	dummy = Node(-1, self.head)
        cur = self.head
        prev = dummy
        while True:
            if cur is None:
                break
            if cur.val == prev.val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next

        self.head = dummy.next


    def slice_to_end(self, from_: int):
        nodes = []
        i = 0
        for node in self:
            if i >= from_:
                nodes.append(node)
            i += 1
        return SingleLinkedList(nodes)

    def slice_to_end_inplace(self, from_: int):
        i = 0
        for node in self:
            if i == from_:
                self.head = node
                break
            i += 1

    def reverse(self):
        nodes = [self.head]
        prev_node = None
        while nodes:
            node = nodes.pop(0)
            if node.next:
                nodes.append(node.next)
            node.next = prev_node
            prev_node = node

        self.head, self.tail = self.tail, self.head

    def get_middle(self):
        fast = slow = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_

    def __repr__(self):
        return f"{self.val}"
