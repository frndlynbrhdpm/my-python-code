# Removal should be in-place

def remove_num_in_array(A,n):
	while A.count(n)>0:
		A.remove(n)
	return A

def remove_num_in_array_2(A,n):
	idx=0

	for i in A:
		if i!=n:
			A[idx]=i
		idx+=1
	del A[idx:]

A=[2,3,2,1,2,3,6]
A=remove_num_in_array(A,2)
print(A)
# print(l)
