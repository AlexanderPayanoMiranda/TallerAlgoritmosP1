# Not working!

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

    def sort(self):
        if not self.head or not self.head.next:
            return
        self._sort(self.head, self.tail)

    def _sort(self, head, tail):
        if head == tail:
            return

        pivot = tail
        prev = head.prev
        current = head

        while current != tail:
            if current.val < pivot.val:
                prev = current
                current = current.next
            else:
                self.remove(current)
                self.add(current.val)
                current = prev.next

        self._sort(head, pivot.prev)
        self._sort(pivot.next, tail)


my_list = DoubleLinkedList()

my_list.add(5)
my_list.add(8)
my_list.add(2)
my_list.add(3)
my_list.add(1)
my_list.add(4)

my_list.sort()

current = my_list.head
while current:
    print(current.val)
    current = current.next
