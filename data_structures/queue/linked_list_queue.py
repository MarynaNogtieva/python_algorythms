class Node:
	def __init__(self, value, next_node=None):
		self.value = value
		self.next = next_node

class Queue:
	def __init__(self,first=None, last=None):
		self.first = None
		self.last = None
		self.length = 0

	def peek(self):
		return self.first

	def enqueue(self, value):
		new_node = Node(value)
		if self.length == 0:
			self.first = new_node
			self.last = new_node
			print(f"first first: {self.first.value}")
			print(f"last: {self.last.value}")
		else:
			print(f"last before: {self.last.value}")
			self.last.next = new_node
			self.last = new_node
			print(f"last after: {self.last.value}")
		self.length += 1
		return self

	def dequeue(self):
		print(f"first before dequeue: {self.first.value}")
		if self.length == 0:
			return None
		first_node = self.first
	
		if self.first == self.last:
			self.first = None
			self.last = None

		if self.first: 
			self.first = self.first.next
			print(f"first after dequeue: {self.first.value}")
		self.length -= 1
		return first_node

	def print_linked_list(self):
		current = self.first
		arr = []
		while(current):
				arr.append(current.value)
				current = current.next
		print(arr)

my_queue = Queue()
my_queue.enqueue('Jane')
my_queue.enqueue('Sam')
my_queue.enqueue('Irene')
my_queue.enqueue('Mike')
my_queue.print_linked_list()
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.print_linked_list()