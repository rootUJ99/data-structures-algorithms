class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class Queue:
	def __init__(self, head=None):
		self.head = head
	
	def enqueue(self, data):
		if self.head == None:
			self.head = Node(data)
			return

		t = self.head
		while t.next:
			t = t.next
		t.next = Node(data)

	def dequeue(self):
		if self.head == None:
			Exception('Queue is empty')
			return
		self.head = self.head.next
		
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
	
	def isEmpty(self):
		return True if self.head == None else False

	def size(self):
		if self.head == None:
			return None
		count = 0 
		t = self.head
		while t.next:
			count += 1
			t = t.next
		return count

q = Queue()

q.enqueue(151)
q.enqueue(11)
q.enqueue(51)
print(q.size())
q.dequeue()
q.print()