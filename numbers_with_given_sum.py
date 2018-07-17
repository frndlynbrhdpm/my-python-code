# Array is sorted
def num_with_given_sum(A,s):
	# mid = len(A)//2
	result=[]

	for i in range(len(A)):
		for j in range(i+1,len(A)):
			if abs(s-A[i])==A[j]:
				result.append(A[i])
				result.append(A[j])

	# Below logic wouldn't work if one number falls in smaller range and the 2nd number is on teh other side
	# if abs(s-A[mid])<A[mid]:
	# 	for i in range(mid):
	# 		for j in range(i+1,mid):
	# 			if abs(s-A[i])==A[j]:
	# 				result.append(A[i])
	# 				result.append(A[j])
	# else:
	# 	for i in range(mid,len(A)):
	# 		for j in range(mid+1,len(A)):
	# 			if abs(s-A[i])==A[j]:
	# 				result.append(A[i])
	# 				result.append(A[j])
	return result

A=[1, 2, 4, 7, 11, 15]
s=16
r=num_with_given_sum(A,s)
print(r)