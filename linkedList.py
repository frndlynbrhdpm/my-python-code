class node:
	def __init__(self, data=None):
		self.data=data
		self.next=None

#ToFix	
def strcmp(l1,l2):
	while l1.next!=None and l2.next!=None:	
		
			if l1.data>l2.data:
				return 1
			elif l2.data>l1.data:
				return -1
			else:
				break

	if (l1 and not l2):
		return 1
	elif (l2 and not l1):
		return -1

	return 0


class linked_list:

	def __init__(self):
		self.head=node()  #because head has no data


	def append(self,data):
		new_node=node(data)   # new node with data
		current = self.head
		while current.next!=None:
			current=current.next
		current.next=new_node

	def display(self):
		arr=[]
		current=self.head
		while current.next!=None:
			current=current.next
			arr.append(current.data)

		print(arr)

	def length(self):
		len=0
		current=self.head
		while current.next!=None:
			len+=1
			current=current.next
		return len

	def delete_node(self,index):
		curr_index=0
		current=self.head
		if index < self.length():
			while current.next!=None:
				last_node=current
				current=current.next
				if curr_index==index:
					last_node.next=current.next
					return
				curr_index+=1
		else:
			print("ERROR!")
			return

	def insert_node(self,data,index):
		curr_index=0
		new_node=node(data)
		current=self.head
		# last_node=self.head
		if index<self.length():
			while True:
				last_node=current
				current=current.next
				if curr_index==index:
					last_node.next=new_node
					new_node.next=current
					return
				curr_index+=1
		else:
			print("ERROR in inserting a node")
			return

	def set(self,data,index):
		curr_index=0
		current=self.head
		if index<self.length():
			while current.next!=None:
				current=current.next
				if curr_index==index:
					current.data=data
					return
				curr_index+=1
		else:
			print("ERROR in inserting a node")
			return

	def insert_in_sorted(self,data):
		new_node=node(data)
		current=self.head
		while current.next!=None:
			last_node=current
			current=current.next
			if current.data>data:
				last_node.next=new_node
				new_node.next=current
				return

def sum(l1, l2):
	len1 = l1.length()-1
	len2 = l2.length()-1
	# print(len1,len2) 
	while len1 <= len2 or len1 >= len2:
		if l1.next==None and 

# L.append('gwi')
# L.append('jce')
# L.append(4)

# L.length()
# L.delete_node(0)
# L.display()
# # L.insert_node(6,1)
# # L.display()
# # L.set(7,3)
# # L.display()
# L.insert_in_sorted(0)
# L.display()

# s1=node('s')
# s1.next=node('h')
# s1.next.next=node('a')

# s2=node('s')
# s2.next=node('h')
# s2.next.next=node('b')
# # s2.next.next.next=node('a')

# r=strcmp(s1,s2)
# print(r)

num1=linked_list()
num2=linked_list()

num1.append(5)
num1.append(4)
num1.append(3)

num2.append(1)
num2.append(2)
num2.append(3)

sum(num1,num2)
