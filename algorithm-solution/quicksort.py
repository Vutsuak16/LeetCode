def partition(A,start,end):

	pivot = A[end]
	partition_index=start
	for i in range(start,end):
		if A[i]<=pivot:
			A[i],A[partition_index]=A[partition_index],A[i]
			partition_index+=1
	A[end],A[partition_index]=A[partition_index],A[end]
	return partition_index


def quicksort(A,start,end):
	if start<end:
		partition_index=partition(A,start,end)
		quicksort(A,start,partition_index-1)
		quicksort(A,partition_index+1,end)
	
A=[1,2,3,4,-1,-2,0,100,0,0,0,23]	
quicksort(A,0,len(A)-1)
print A



