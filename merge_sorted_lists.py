def merge_sorted_lists(l1,l2):
	l=[] #result
	i,j=0,0 #respective pointers for l1 and l2

	for k in range(len(l1)+len(l2)):
		if l1[i]<=l2[j]:
			l[k]=l1[i]
			i+=1
		else:
			l[k]=l2[j]
			j+=1
	return l

def merge_sorted_lists_2(l1,l2):
	l=[]

	while len(l1)>0 and len(l2)>0:
		if l1[0]<=l2[0]:
			l.append(l1[0])
			l1=l1[1:]
		else:
			l.append(l2[0])
			l2=l2[1:]

	if len(l1)>0:
		l.append(l1)
	if len(l2)>0:
		l.append(l2)	


l1=[3, 4, 6, 10, 11, 9]
l2=[1, 5, 8, 12, 14, 19]
l=merge_sorted_lists(l1,l2)
print(l)