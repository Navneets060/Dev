
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

def diameter(root):

	if root == None:
		return 0
	
	lheight = height(root.left)
	rheight = height(root.right)

	ldiameter = diameter(root.left)
	rdiameter = diameter(root.right)

	return max(lheight + 1 + rheight, max(ldiameter, rdiameter))

if __name__ == "__main__":

	root = Node(10)
	root.left = Node(20)
	root.left.left = Node(30)
	print(height(root))
	'''
		root.left = Node(20)
		root.right = Node(30)
		root.left.left = Node(25)
		root.left.right = Node(15)		
		root.right.left = Node(35)
		root.right.right = Node(28)
		root.right.right.right = Node(50)
		root.right.left.right = Node(70)
		print(diameter(root))
	'''	
							