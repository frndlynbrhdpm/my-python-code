class node:
	def __init__(self, val):
		self.val=val
		self.next=None
	
class Solution:
	def contains_cycle(self, head):
		curr=head
		
		while curr.next!=None:
			curr=curr.next
			if curr.next==head:
				return True
		return False
	
#Driver code
a=node(1)
b=node(2)
c=node(3)
d=node(4)
e=node(5)

a.next=b
b.next=c
c.next=d
d.next=e
e.next=a

s=Solution()
print(s.contains_cycle(a))
