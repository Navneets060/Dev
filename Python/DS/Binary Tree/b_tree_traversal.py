
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def inorder_traversal(root):
	if root == None:
		return
	inorder_traversal(root.left)
	
	print(root.val, end=" ")

	inorder_traversal(root.right)		

def preorder_traversal(root):
	if root == None:
		return
	print(root.val, end=" ")

	preorder_traversal(root.left)
	
	preorder_traversal(root.right)

def postorder_traversal(root):
	if root == None:
		return
	print(root.val, end=" ")

	postorder_traversal(root.right)

	postorder_traversal(root.left)

if __name__ == "__main__":
	root = Node(10)
	root.left = Node(20)
	root.right = Node(30)
	root.left.left = Node(25)
	root.left.right = Node(15)		
	root.right.left = Node(35)
	root.right.right = Node(28)	
	print(" inorder_traversal : ", end ="")
	inorder_traversal(root)
	print("\n","preorder_traversal : ", end = "")
	preorder_traversal(root)
	print("\n","postorder_traversal : ", end ="")
	postorder_traversal(root)