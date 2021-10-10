class Node:

	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


class LinkedList:

	def __init__(self):
		self.head = None

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

	def length(self):
		n = self.head
		count = 0
		while n:
			count+=1
			n = n.next
		return count

	def shift(self, data):
		self.head = Node(data, self.head)
	
	def push(self, data):

		if self.head == None:
			self.shift(data)
			return
		t= self.head
		while t.next:
			t = t.next
		t.next = Node(data, None)

	def remove_at_index(self, index):
		if index<0 or index>=self.length():
			raise Exception("Invalid Index")
		if index == None:
			print('can nor delete from empty list')
			return 
		if index == 0:
			self.head = self.head.next
			return
		count = 0
		itr = self.head
		while itr:
			if (count == index-1):
				itr.next = itr.next.next
				break
			itr = itr.next
			count += 1
	
	def push_list(self, values):
		if type(values) is list:
			for value in values:
				self.push(value)
		else: 
			Exception('Provide list as argument')

	def remove_by_value(self, value):
		itr = self.head
		count = 0
		while(itr):
			if itr.data == value:
				itr.next = itr.next.next
			else: 
				itr = itr.next

if __name__ == "__main__":

	ll = LinkedList()

	ll.push(20)

	ll.push(50)
	ll.shift(35)
	ll.length()
	ll.print()
	# ll.remove_at_index(0)
	ll.remove_by_value(50)
	ll.push_list([21,43,43,43])
	ll.print()


