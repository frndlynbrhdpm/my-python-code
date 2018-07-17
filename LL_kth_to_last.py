class linked_list_node:
	def __init__(self,val):
		self.val=val
		self.next=None

def kth_to_last(k,head):
	curr=head
	A=[]

	while curr.next!=None:
		curr=curr.next
		A.append(curr.val)

	if len(A)>0:
		return A[len(A)-k]
	else:
		return 0

def kth_to_last_ver2(k, head):
	curr=head

	while curr.next!=None:
		curr=curr.next
		k-=1
		if k==-1:
			return curr.val
	return 0


a=linked_list_node("violet")
b=linked_list_node("indigo")
c=linked_list_node("blue")
d=linked_list_node("green")
e=linked_list_node("yellow")

a.next=b
b.next=c
c.next=d
d.next=e 

kth=kth_to_last(2,a)
kth_2=kth_to_last_ver2(2,a)

print(kth)
print(kth_2)

	
		