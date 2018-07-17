class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def is_valid_bst(self,root,floor=float('-inf'),ceiling=float('inf')):
        if root==None:
            return True
        elif root.val<=floor or root.val>=ceiling:
            return False
        else:
            return self.is_valid_bst(root.left,floor,root.val) and self.is_valid_bst(root.right,root.val,ceiling)


a=node(8)
b=node(3)
c=node(10)
d=node(1)
e=node(6)
# f=node(None)
g=node(14)
# h=node(None)
# i=node(None)
j=node(4)
k=node(7)
l=node(13)
# m=node(None)


a.left=b
a.right=c
b.left=d
b.right=e
d.left=None
d.right=None
e.left=j
e.right=k
c.left=None
c.right=g
g.left=l
g.right=None

s=Solution()
print(s.is_valid_bst(a))

# 
# Your previous Python 2 content is preserved below:
# 
# # This is a sandbox to experiment with CoderPad's execution capabilities.
# # It's a temporary, throw-away session only visible to you.
# 
# def say_hello():
#     print 'Hello, World'
# 
# for i in xrange(5):
#     say_hello()
# 
