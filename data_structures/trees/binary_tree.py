class Node:
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, value):
		node = Node(value)
		if self.root == None:
			self.root = node
			return
		else:
			current_node = self.root
			while(current_node.left != node) and (current_node.right != node):
				if node.value > current_node.value:
					# append to the right
					if current_node.right == None:
						current_node.right = node
					else:
						current_node = current_node.right
				elif node.value < current_node.value:
					# append to the right
					if current_node.left == None:
						current_node.left = node
					else:
						current_node = current_node.left
		return self

	def lookup(self, value):
		if self.root == None:
			return
		else:
			current_node = self.root
			while current_node:
				if current_node.value == value:
				  print('Found')
				  return current_node.value 
				elif value > current_node.value:
					current_node = current_node.right
				elif value < current_node.value:
					current_node = current_node.left
			print('Not Found')
			return

def traverse(tree):
    if tree.left is not None:
        yield from traverse(tree.left)

    yield tree.value

    if tree.right is not None:
        yield from traverse(tree.right)

bst = BinarySearchTree()
bst.insert(5)
bst.insert(4)
bst.insert(34)
bst.lookup(3)
bst.lookup(34)
bst.lookup(5)
bst.insert(3)

print(list(traverse(bst.root)))

