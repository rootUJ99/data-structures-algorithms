from ctypes import pointer


class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class CircularLinkedList:
	def __init__(self, head=None):
		self.head = head
	
	def print(self):
		if self.head == None:
			print('List is empty')
			return
		n = self.head
		llist = ''
		while n:
			llist = f"{llist} {str(n.data)} {'-->' if n.next != None else ''}"
			n = n.next
			if (self.checkLoop(n, n.next)):
				break
		return print(llist)

	def checkLoop(self):
		pointer1 = self.head
		pointer2 = self.head

		while(pointer1 and pointer2 and pointer2.next):
			
			pointer1 = pointer1.next
			pointer2 = pointer2.next.next

			if(pointer1 == pointer2):
				print(pointer1 == self.head)
				print(pointer2 == self.head)
				print(pointer1 == self.head and pointer2 == self.head)

				print("loop detected")
				return True

	def push(self, data):
		if self.head == None:
			self.head = Node(data, self.head)
			return
			
		n = self.head
		while n.next:
			print(n.data)
			if (n.next == self.head):
				break
			n = n.next
		n.next = Node(data, self.head)
		print(n.data)



cl = CircularLinkedList()

cl.push(2) # p1 = 2
cl.push(3)
cl.push(4)
cl.push(5)
cl.checkLoop()
