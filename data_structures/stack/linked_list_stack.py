class Node:
		def __init__(self, value, next_node=None):
				self.value = value
				self.next = next_node

class Stack:
		def __init__(self, top=None, bottom=None):
				self.top = top
				self.bottom = bottom
				self.length = 0

		def push(self, value):
			new_node = Node(value)
			if self.length == 0:
				self.bottom = new_node
				self.top = new_node
				print(f"top first: {self.top.value}")
			else:
				print(f"top before: {self.top.value}")
				holding_point = self.top
				self.top = new_node
				print(f"top after: {self.top.value}")
				self.top.next = holding_point
			
			self.length += 1
			return self


		def pop(self):
			if self.length == 0:
				return None
			top_node = self.top
			self.top = top_node.next
			# print(self.top.value)
			self.length -= 1
			if self.top == self.bottom:
				self.bottom = None
			return top_node

		def peek(self):
			return self.top

		def print_linked_list(self):
			current = self.top
			arr = []
			while(current):
					arr.append(current.value)
					current = current.next
			print(arr)
    

my_stack = Stack()
my_stack.push('google')
my_stack.push('udemy')
my_stack.push('youtube')
my_stack.push('discord')
my_stack.print_linked_list()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.print_linked_list()