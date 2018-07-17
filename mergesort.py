
def merge_sort(A):
	merge_sort2(A, 0, len(A)-1)  # 0-7
	
def merge_sort2(A, first, last):
	if first < last:  # 0<7
		middle = (first + last)//2  # 0+7 //2
		merge_sort2(A, first, middle) # 0-3 both included
		merge_sort2(A, middle+1, last) #4-7 both included
		merge(A, first, middle, last) # 0, 3, 7
		
def merge(A, first, middle, last):  # 0, 3, 7
	L = A[first:middle+1]  # 0-4 (4 not included)
	R = A[middle+1:last+1] # 4-8 (8 not included)
	L.append(99999999)
	R.append(99999999)
	i = j = 0
	
	for k in range (first, last+1):  #(0, 8]
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
			
A = [5,9,1,2,4,8,6,3,7]	
print(A)
merge_sort(A)
print(A)