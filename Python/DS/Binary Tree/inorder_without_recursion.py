
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

# Iterative function for inorder tree traversal
def inorder(root):

    temp = root 
    s = [] # initialize stack
    done = 0
     
    while(not done):
         
        # Reach the left most Node of the temp Node
        if temp != None:

            s.append(temp)         
            temp = temp.left 

        else:
            if(len(s) >0 ):
                temp = s.pop()
                print(temp.val)
                temp = temp.right 
 
            else:
                done = 1				

if __name__ == "__main__":
	root = Node(10)
	root.left = Node(20)
	root.right = Node(30)
	root.left.left = Node(25)
	root.left.right = Node(15)		
	root.right.left = Node(35)
	root.right.right = Node(28)
	root.right.right.right = Node(50)
	root.right.left.right = Node(70)
	inorder(root)		