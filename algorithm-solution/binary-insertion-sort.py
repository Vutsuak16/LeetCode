

def binary_search(val,l):

	start=0
	end=len(l)-1
	mid=(start+end/2)

	while start<=end:

		if val==l[mid]:
			return mid
			break
		elif val<l[mid]:
			end=mid-1
		else:
			start=mid+1

		mid= (start+end)/2

	return mid+1




def binary_insertion_sort(l):

	for i in range(1,len(l)):

		key=l[i]
		insert_pos=binary_search(key,l[:i])
		
		for j in range(i,insert_pos,-1):
			l[j],l[j-1]=l[j-1],l[j]

		



