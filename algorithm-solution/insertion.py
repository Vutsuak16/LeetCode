def insertion(A):
	for i in range(1,len(A)):
		curr_value=A[i]
		position=i
		while position>0 and A[position-1]>curr_value:
			A[position]=A[position-1]
			position-=1
		A[position]=curr_value

A=[1,2,3,-1,0,10000,1]
insertion(A)
print A



