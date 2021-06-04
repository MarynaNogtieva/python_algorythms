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

    def insert(self, value, index):
        if index >= self.length:
            self.append(value)
            return
        elif index <= 0:
            self.prepend(value)
            return

        # node that will be before the newly inserted node
        prev_node = self.traverse_to_index(index-1)
        new_node = Node(value)
       
        # holding_pointer - node that occupies given index
        # and will be located after the newly inserted node
        holding_pointer = prev_node.next
        prev_node.next = new_node
        new_node.next = holding_pointer

        self.length += 1
    
    def remove(self, index):
        if index <= 0: 
            new_head = self.head.next
            self.head = new_head
        elif index > self.length:
            index = self.length-2

        prev_node = self.traverse_to_index(index -1)
        node_to_remove = prev_node.next
        next_node = node_to_remove.next
        prev_node.next = next_node

        self.length -= 1


    def print_linked_list(self):
        current = self.head
        while(current):
            print(current.value)
            current = current.next
    
    def traverse_to_index(self, index):
        current_node = self.head
        for i in range(index):
            # print(f"current_node: {current_node.value}, index: {i}")
            current_node = current_node.next 
        return current_node


ll = LinkedList()
# ll.prepend(11)
print("--------ADD---------")
ll.append(1)
ll.append(5)
ll.append(4)
ll.prepend(11)
ll.insert(23, 2)
ll.insert(26, 10)
ll.insert(7,0)
ll.print_linked_list()
print("--------REMOVE---------")
ll.remove(-2)
ll.remove(1)
ll.remove(90)
ll.print_linked_list()
