class Stack:
		def __init__(self):
				self.array = []
				self.length = 0

		def push(self, value):
			self.array.append(value)	
			self.length += 1
			return self


		def pop(self):
			res = self.array.pop()
			self.length -= 1
			return res

		def peek(self):
			return self.array[self.length-1]

    

my_stack = Stack()
my_stack.push('google')
my_stack.push('udemy')
my_stack.push('youtube')
my_stack.push('discord')
print(my_stack.array)
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack.array)