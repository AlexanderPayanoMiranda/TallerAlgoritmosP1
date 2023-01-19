class Node:
    def __init__(self, data=None):
        self.prev = None
        self.data = data
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head_val = None

    def double_linked_list_print(self):
        print_val = self.head_val
        while print_val is not None:
            print(print_val.data)
            print_val = print_val.next

    def insert_node_at_beginning(self, new_data):
        new_node = Node(new_data)
        if self.head_val is None:
            self.head_val = new_node
        else:
            new_node.next = self.head_val
            self.head_val.prev = new_node
            self.head_val = new_node

    def insert_node_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head_val is None:
            self.head_val = new_node
        last_node = self.head_val

        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def insert_node_in_between(self, middle_node, new_data):
        if middle_node is None:
            print("No existe el nodo!")

        new_node = Node(new_data)
        new_node.next = middle_node.next
        middle_node.next.prev = new_node
        middle_node.next = new_node

    def remove_node(self, remove_data):
        head_val = self.head_val

        if head_val is not None:
            if head_val.data == remove_data:
                head_val.next.prev = None
                self.head_val = head_val.next
                return
        prev = None
        while head_val is not None:
            if head_val.data == remove_data:
                head_val.next.prev = prev
                prev.next = head_val.next
                break
            prev = head_val
            head_val = head_val.next


lista1 = DoubleLinkedList()

e1 = Node("1")
e3 = Node("3")

e1.next = e3

e3.prev = e1

lista1.head_val = e1

lista1.insert_node_at_beginning("0")
lista1.insert_node_in_between(e1, "2")
lista1.insert_node_at_end("4")
lista1.remove_node("3")

lista1.double_linked_list_print()
