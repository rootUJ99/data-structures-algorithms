from ctypes import pointer


class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class CircularLinkedList:
	def __init__(self, head=None):
		self.head = head
		self.last = None
	
	def print(self):
		if self.head == None:
			print('List is empty')
			return
		n = self.head
		llist = ''
		while n.next:
			llist = f"{llist} {str(n.data)} {'-->' if n.next != self.head else ''}"
			n = n.next
			if n == self.head:
				break
		return print(llist)

	def checkLoop(self, pointer=None):
		pointer1 = pointer or self.head
		pointer2 = pointer or self.head

		while(pointer1 and pointer2 and pointer2.next):
			print(pointer1.data, 'ptr1')
			
			pointer1 = pointer1.next
			pointer2 = pointer2.next.next
			if(pointer1 == pointer2):
				print("loop detected")
				return True

	def push(self, data):
		if self.head == None:
			self.head = Node(data, self.head)
			self.last = self.head
			return
			
		# n = self.head
		# while n.next:
		# 	if (n.next == self.head):
		# 		break
		# 	n = n.next
		new_node = Node(data, self.last.next)
		self.last.next = new_node
		self.last = new_node
		new_node.next = self.head


	def shift(self, data):
		if self.head ==None:
			self.head = Node(data, self.head)
			self.last = self.head
			return
		new_node = Node(data, self.last.next)
		self.head = new_node
		self.last.next = new_node




cl = CircularLinkedList()

cl.push(2) # p1 = 2
cl.push(3)
cl.push(4)
print(cl.head.data)
cl.push(5)
cl.shift(1)
cl.shift(0)
cl.print()
cl.checkLoop()
