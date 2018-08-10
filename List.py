class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self, head):
		self.head = head

	def addElement(self, node):
		current = self.head
		while current.next != None:
			current = current.next

		current.next = node

	def print(self):
		current = self.head
		while current!=None:
			print(current.data)
			current = current.next

	def reverse(self):
		prev = None
		aft = self.head.next

		while aft != None:
			self.head.next = prev
			prev = self.head
			self.head = aft
			aft = self.head.next
			self.head.next = prev

	def removeDuplicate(self):
		current = self.head

		while current != None:
			traveler = current.next
			prev = current
			
			while traveler != None:
				if traveler.data == current.data :
					prev.next = traveler.next
					traveler = traveler.next
				else:
					prev = prev.next
					traveler = traveler.next
				

			current = current.next

	def getLength(self):
		length = 0
		current = self.head

		while current!=None:
			length += 1
			current = current.next

		return length

	def getKfromLast(self, k):
		length = self.getLength()

		n = length - k + 1

		current = self.head
		while n>1:
			current = current.next
			n -= 1

		return current.data

	def getKfromLastOpt(self, k):
		p1 = self.head
		p2 = self.head

		for i in range(1, k):
			p1 = p1.next

		while p1.next != None:
			p1 = p1.next
			p2 = p2.next

		return p2.data

def main():
	node1 = Node(10)
	mylist = LinkedList(node1)

	for i in range(2, 11):
		mylist.addElement(Node(i))
	
	for i in range(2, 11):
		mylist.addElement(Node(i))

	mylist.print()
	print('-----------')
	
	print(mylist.getKfromLastOpt(3))

if __name__ == '__main__':
	main()