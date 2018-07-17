def max_in_windows(A,l):
	result=[]
	for i in range(len(A)-1):
		temp=A[i:i+l]
		temp=sorted(temp)
		result.append(temp[-1])
	return result
		# for j in range(len(temp)):

A=[2, 3, 4, 2, 6, 2, 5]
B=max_in_windows(A,3)
print(B)