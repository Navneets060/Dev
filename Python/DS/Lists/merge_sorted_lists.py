class Node:
	def __init__(self,data=None):
		self.data = data
		self.next = None

class linked_list:
	def __init__(self):
		self.head = None

	def merge_sorted_lists(self, list1, list2): 
		temp = self.head
		self.head = temp

		while (list1.next != None and list2.next != None):
			if list1.data <= list2.data:
				temp = list1
				list1 = list1.next
			else:
				temp= list2
				list2 = list2.next
			temp = temp.next	
				
		if(list1 == None):
			temp = list2
		else:
			temp = list1	

	def print_list(self):
		temp = self.head
		while temp != None:
			print(temp.data)
			temp = temp.next

if __name__ == "__main__":
	print("First sorted list")
	l1 = linked_list()
	l1.head = Node(10)
	l1.head.next = Node(20)
	l1.print_list()
	print("Second sorted list")
	l2 = linked_list()
	l2.head = Node(15)
	l2.head.next = Node(25)
	l2.print_list()
	print("List after merging")
	l3 = linked_list()
	l3.merge_sorted_lists(l1.head, l2.head)
	l3.print_list()

