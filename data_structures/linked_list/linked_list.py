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
            return
        elif index > self.length:
            index = self.length-1

        prev_node = self.traverse_to_index(index -1)
        node_to_remove = prev_node.next
        next_node = node_to_remove.next
        prev_node.next = next_node

        self.length -= 1

    def reverse(self):
        if not self.head.next:
            return

        first = self.head
        self.tail = self.head
        second = first.next
        print(f"first: {first.value}")
        print(f"head: {self.head.value}")
        print(f"tail: {self.tail.value}")
        print(f"second: {second.value}")
        while (second):
            print("-----START LOOP---------")
            temp = second.next
            if temp: print(f"temp: {temp.value}")
            second.next = first
            print(f"second.next: {second.next.value}")
            first = second
            print(f"first: {first.value}")
            second = temp
            if second: print(f"second: {second.value}")
            if temp: print(f"end temp: {temp.value}")
            print("-----END LOOP---------")
        
        print(f"before None - self.head.next.value: {self.head.next.value}")
        print(f"before None - self.tail.value: {self.tail.value}")
        print(f"before None - self.tail.next.value: {self.tail.next.value}")
        self.head.next = None
        print(f"after None - self.tail.value: {self.tail.value}")
        
        self.head = first
        print(f"self.head: {self.head.value}")
        print(f"after - self.head.next: {self.head.next.value}")
        


    def print_linked_list(self):
        current = self.head
        arr = []
        while(current):
            arr.append(current.value)
            current = current.next
        print(arr)
    
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
# ll.remove(-2)
# ll.remove(1)
ll.remove(90)
ll.print_linked_list()
# print("--------REVERSE---------")
# ll.reverse()
# ll.print_linked_list()