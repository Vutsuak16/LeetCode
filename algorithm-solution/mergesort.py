def merge(a,b):
	c=[0]*(len(a)+len(b))
	
	i=0
	j=0
	k=0

	while i<len(a) and j<len(b):

		if a[i]<b[j]:
			c[k]=a[i]
			i+=1
		else:
			c[k]=b[j]
			j+=1

		k+=1



	while i<len(a):
		c[k]=a[i]
		k+=1
		i+=1

	while j<len(b):
		c[k]=b[j]
		j+=1
		k+=1


	return c



def merge_sort(l):

	if len(l)==0 or len(l)==1:
		return l
	else:
		mid=len(l)/2
		a=merge_sort(l[:mid])
		b=merge_sort(l[mid:])
		return merge(a,b)


print merge_sort([100,10,-1,0,1,2])
