def reverse_string(str):
	res = ""
	low=0
	high=len(str)-1

	while low<=high:
		res+=str[high]
		high-=1

	return res

s="Madam, I'm Adam"
print(reverse_string(s))
