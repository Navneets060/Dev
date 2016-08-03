class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class linked_list:
	def __init__(self):
		self.head = None

	def ll_reverse(self, curr, prev):
		if curr.next == None:
			self.head = curr
			curr.next = prev
			return
		self.ll_reverse(curr.next, curr)
		curr.next = prev

	def print_list(self):
		temp = self.head
		while temp != None:
			print(temp.data)
			temp = temp.next

if __name__ == "__main__":
	l = linked_list()
	l.head = Node(10)
	l.head.next = Node(20)
	l.head.next.next = Node(30)
	l.head.next.next.next = Node(40)
	l.print_list()
	l.ll_reverse(l.head, None)
	print("After List revarsal :")
	l.print_list()

