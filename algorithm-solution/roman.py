

def romanToInt(s):

	sum =0

	k={"I":1,"IV":4,"IX":9,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
	l=list(s)
	flg=0
	for i in range(len(l)):
		if flg==1:
			flg=0
			continue
		if i != len(l)-1:
			if k[l[i+1]] > k[l[i]]:
				sum+=k[l[i+1]]-k[l[i]]
				flg=1
				
				continue
			else:
				sum+=k[l[i]]
				
		else:
			sum+=k[l[i]]

	print sum
			




s=input("enter_roman")
romanToInt(s)
