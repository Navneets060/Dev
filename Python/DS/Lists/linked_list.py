
#represents a single Node			
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

#Linked List Basic program
class linked_list:

	def __init__(self,data = None):
		if data != None:
			self.head = Node(data)
		else:
			self.head = None

	def print_list(self):
		node = self.head
		if node == None:
			print("List Empty")
			return

		while node:
			print(node.data)
			node = node.next

	def add_node(self, data):
		if self.head == None:
			self.head = Node(data)
		else:
			temp = self.head
			while(temp.next != None):
				temp = temp.next
			temp.next = Node(data)	

	def delete_node(self, x):
		if self.head == None:
			print("List Empty !! nothing to delete")
		else:
			prev = None
			current = self.head
			while(current.data != x and current.next != None):
				prev = current
				current = current.next
			if current.data == x:
				print("deleting node with value" + str(x))
				prev.next = current.next
			else:
				print("Number not found")		

	def reverse_list(self):
		if self.head == None:
			print("List is Empty")
		else:
			temp = self.head
			current = temp
			prev = None
			while current != None:
				temp = current.next
				current.next = prev
				prev = current
				current = temp
			self.head = prev		

	def list_insertion_by_choice(self, data):
		choice = int(input("Enter your choice : 1 for insertion as head, 2 for in between , 3 for at last ::"))	
		if choice == 1:
			temp = Node(data)
			x = self.head
			self.head = temp
			self.head.next = x

		elif choice == 2 :
			num = int(input("Enter the data after which the insertion should take place :"))
			prev = self.head
			current = self.head
			while(current.data != num and current.next != None):
				prev = current
				current = current.next
			if current.data == num:
				prev.next = Node(data)
			else:
				print("Number not found")
		elif choice == 3 :
			self.add_node(data)
		else:
			print("wrong choice selected")

# main method to execute the program
if __name__ == '__main__':
	lis=linked_list(20)
	lis.add_node(30)
	lis.add_node("nav")
	lis.delete_node(30)
	lis.add_node(50)
	lis.print_list()
	print(" reversing the list now")
	lis.reverse_list()
	lis.print_list() 
	lis=linked_list(20)
	lis.list_insertion_by_choice(30)
	lis.print_list()


