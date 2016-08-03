class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def height(root):
	if root == None:
		return 0
	lheight = height(root.left)
	rheight = height(root.right)

	if lheight > rheight:
		return lheight + 1
	else:
		return rheight + 1		


def level_order_traversal(root):
	for level in range(height(root)+1):
		print_traversal(root, level)

def print_traversal(root, level):
	if root == None:
		return
	if level == 1:
		print(root.val)
	elif level > 1:
		print_traversal(root.left, level-1)
		print_traversal(root.right, level-1)		

def level_traversal_queue(root):
	if root == None:
		return
	queue = []

	queue.append(root)

	while len(queue) > 0:
		print(queue[0].val)
		node = queue.pop(0)

		if node.left is not None:
			queue.append(node.left)
		if node.right is not None:
			queue.append(node.right)

if __name__ == "__main__":
	root = Node(10)
	root.left = Node(20)
	root.right = Node(30)
	root.left.left = Node(25)
	root.left.right = Node(15)		
	root.right.left = Node(35)
	root.right.right = Node(28)
	root.right.right.right = Node(50)
	root.left.left.right = Node(40)
	level_order_traversal(root)
	print("--------------------------------------")
	level_traversal_queue(root)			
