class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head_val = None

    def linked_list_print(self):
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
            self.head_val = new_node

    def insert_node_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head_val is None:
            self.head_val = new_node
        last_node = self.head_val

        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_node_in_between(self, middle_node, new_data):
        if middle_node is None:
            print("No existe el nodo!")

        new_node = Node(new_data)
        new_node.next = middle_node.next
        middle_node.next = new_node
        print()

    def remove_node(self, remove_data):
        head_val = self.head_val

        if head_val is not None:
            if head_val.data == remove_data:
                self.head_val = head_val.next
                return
        prev = None
        while head_val is not None:
            if head_val.data == remove_data:
                prev.next = head_val.next
                break
            prev = head_val
            head_val = head_val.next


e1 = Node("Lunes")
e2 = Node("Martes")
e3 = Node("Jueves")

list1 = LinkedList()
list1.head_val = e1

list1.head_val.next = e2
e2.next = e3

list1.insert_node_at_beginning("Domingo")

list1.insert_node_in_between(e2, "Miercoles")

list1.insert_node_at_end("Viernes")

list1.remove_node("Martes")

list1.linked_list_print()
