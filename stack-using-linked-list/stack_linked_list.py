class Node:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next # next is acting like previous here
class Stack:
	def __init__(self):
		self.top = None
		self.size = -1

	def push(self, data):
		if self.top == None:
			self.top = Node(data)
			self.size +=1
			return
		old_node = self.top
		new_node = Node(data, old_node)
		self.top = new_node
		self.size +=1
	
	def pop(self):
		if self.is_empty():
			Exception('Stack is empty')
			return
		self.top = self.top.next
		self.size -=1
		
	
	def peek(self):
		if not self.is_empty():
			return self.top.data

	def is_empty(self):
		return True if self.top == None else False

	def print(self):
		if self.is_empty():
			print('List is empty')
			return
		n = self.top
		llist = ''
		while n:
			el = '\n'
			llist = f"{llist} {'|' + str(n.data) + '|'} { el +'-----'+el if n.next != None else el}"
			n = n.next
		return print(llist)

s = Stack()
s.push(3)
s.push(4)
s.push(5)
s.push(7)
s.push(8)
s.push(9)
s.pop()
s.pop()

print('top is at',s.peek())

print('size', s.size)

s.print()

		