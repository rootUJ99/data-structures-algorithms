class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class Queue:
	def __init__(self):
		self.front = None
		self.rear = None
	
	def enqueue(self, data):
		if self.is_empty():
			node = Node(data)
			self.front = node
			self.rear = node
			return
		node = Node(data)
		self.rear.next = node
		self.rear = node

	def dequeue(self):
		if self.is_empty():
			self.rear = None
			Exception('Queue is empty')
			return
		self.front = self.front.next

	def rear_data(self):
		return self.rear.data

	def front_data(self):
		return self.front.data
		
	def print(self):
		if self.is_empty():
			print('List is empty')
			return
		n = self.front
		llist = ''
		while n:
			llist = f"{llist} {str(n.data)} {'-->' if n.next != None else ''}"
			n = n.next
		return print(llist)
	
	def is_empty(self):
		return True if self.front == None else False

	def size(self):
		if self.front == None:
			return -1 
		count = 0 
		node = self.front
		while node:
			count += 1
			node = node.next
		return count

q = Queue()

q.enqueue(151)
q.enqueue(11)
q.enqueue(51)
print(q.rear_data())
print(q.front_data())
print(q.size())
q.dequeue()
print(q.front_data())
q.print()