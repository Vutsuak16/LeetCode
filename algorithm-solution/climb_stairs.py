def climb_ways(n):
	l=[1,2,4]
	if n==1:
		return l[0]
	elif n==2:
		return l[1]
	elif n==3:
		return l[2]
	else:
		for i in range(3,n):
			l.append(l[i-1]+l[i-2]+l[i-3])
	return l[-1]


print climb_ways(4)