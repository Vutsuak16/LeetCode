arr = [1, 3, 5, 5, 5, 5 ,67, 123, 125]
#input =5
#output= (2,5)


def first_binary_search(arr,element):
	start=0
	end=len(arr)-1
	while start<=end:
		mid=(start+end)/2
		if mid==0 or arr[mid-1]<element and arr[mid]==element:
			return mid
		elif arr[mid]>element or arr[mid-1]==element:
			end=mid-1
		else:
			start=mid+1

	return mid


def last_binary_search(arr,element):
	start=0
	end=len(arr)-1
	while start<=end:
		mid=(start+end)/2
		if mid==len(arr)-1 or arr[mid+1]>element and arr[mid]==element:
			return mid
		elif arr[mid]<element or arr[mid+1]==element:
			start=mid+1
		else:
			end=mid-1

	return mid


print first_binary_search(arr,5)
print last_binary_search(arr,5)