class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    # add value to the end of the linked list
    def append(self, value):
        node = Node(value)
        if self.tail:
            # append new node to tail
            self.tail.next = node
            # make new node become a tail
            self.tail = node
        else:
            self.head = node
            self.tail = self.head
        self.length += 1
        
        return self
    # add value at the beginning of the list
    def prepend(self, value):
        node = Node(value)
        if self.head:
            next_node = self.head
            node.next = next_node
            self.head = node
        else:
            self.head = node
            self.tail = self.head
        self.length += 1

    def print_linked_list(self):
        current = self.head
        while(current):
            print(current.value)
            current = current.next


ll = LinkedList()
# ll.prepend(11)
ll.append(1)
ll.append(5)
ll.append(4)
ll.print_linked_list()
ll.prepend(11)
ll.print_linked_list()
