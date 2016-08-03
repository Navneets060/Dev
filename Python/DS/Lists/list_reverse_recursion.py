#represents a single Node			
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

#Linked List Basic program
class linked_list:

	def __init__(self):
		self.head = None

	def list_reverse_recur(self, temp = None):
		if temp == None:
			return
		self.list_reverse_recur(temp.next)
		if temp != None:
			print(temp.data)

	def print_list(self):
		node = self.head
		if node == None:
			print("List Empty")
			return

		while node:
			print(node.data)
			node = node.next

if __name__ == "__main__":
	l = linked_list()
	l.head = Node(10)
	l.head.next = Node(20)
	l.head.next.next = Node(30)
	l.print_list()
	print("After Reversal")
	l.list_reverse_recur(l.head)	
