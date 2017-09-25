l=[1,2,3,3,1,1,4,4,5,6,0,12]
k=set()
result=set()
for i in l:
	k2=len(k)
	k.add(i)	
	if (k2)==len(k):
		result.add(i)
			
print list(result)
