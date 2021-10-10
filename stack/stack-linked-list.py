class Node:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

class Stack:
	def __init__(self, head=None):
		self.head = head

	def push(self, data):
		if self.head == None:
			self.head = Node(data)
			return
		t = self.head
		while t.next:
			t = t.next
		t.next = Node(data)
	
	def pop(self):
		if self.head == None:
			Exception('Stack is empty')
			return
		t = self.head
		count = 0
		while t.next:
			if self.size() -1 == count:
				t.next = None
				return
			t = t.next
			count+=count
		print(t)
	
	def peek(self):
		if self.head == None:
			return None
		t = self.head
		while t.next:
			t = t.next
		return t.data

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

	def print(self):
		if self.head == None:
			print('List is empty')
			return
		n = self.head
		llist = ''
		while n:
			el = '\n'
			llist = f"{llist} {'|' + str(n.data) + '|'} { el +'---'+el if n.next != None else el}"
			n = n.next
		return print(llist)

s = Stack()
s.push(5)
s.push(2)
# s.pop()
print(s.size())
print(s.peek())
s.print()

		