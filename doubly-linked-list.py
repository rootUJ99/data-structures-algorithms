class Node:
	def __init__(self, data, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev = prev

	
class DLinkedList:
	def __init__(self, head=None):
		self.head = head
		self.tail = None

	def push(self, data):
		if self.head == None:
			self.head = Node(data)
			return
		t = self.head
		while t.next:
			t = t.next
		t.next = Node(data, None, t)
		self.tail = t.next

	def print_f(self):
		n = self.head
		llistf = ''
		while n:
			llistf = f"{llistf} {str(n.data)} {'-->' if n.next != None else ''}"
			n = n.next
		print(llistf)
	def print_b(self):
		l = self.tail
		llistl = ''
		while l:
			llistl = f"{llistl} {str(l.data)} {'<--' if l.prev != None else ''}"
			l = l.prev
		print(llistl)

	def reverse(self):
		curr = self.head
		prev = None
		next = None
		while curr:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		self.head = prev
d = DLinkedList()

d.push(23)
d.push(64)
d.push(33)
d.push(76)
d.push(90)
d.print_f()
d.print_b()
d.reverse()
d.print_f()
