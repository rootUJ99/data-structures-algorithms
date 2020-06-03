class Node:
	def __init__(self, next=None, prev=None):
		self.next = next
		self.prev = prev

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
		return print(llist)

	# def checkLoop(self, )