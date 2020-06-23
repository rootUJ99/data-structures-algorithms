class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class CLinkedLinst:
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

	def checkLoop(self, slow, fast):
		if (slow == None or fast == None):
			return False
		while(slow != fast):
			if (slow == None or fast == None):
				return False
			slow= slow.next
			fast= fast.next.next
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



cl = CLinkedLinst()

cl.push(2)
cl.push(3)
cl.push(4)
cl.push(5)

cl.print()