def rev_list(li):
	left_idx=0
	right_idx=len(li)-1
	while left_idx<right_idx:
		li[left_idx],li[right_idx]=li[right_idx],li[left_idx]
		left_idx+=1
		right_idx-=1
	return li

a=['a','b','c','d','e']
print(rev_list(a))