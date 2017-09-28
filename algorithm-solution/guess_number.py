 def guessNumber(n):
        
        l,r=1,n   #all natural numbers are sorted
        
        while l<=r:
            mid=(l+r)/2
            number=guess(mid)
            if number==0:
                return mid
            elif number<0:
                r=mid-1
            else:
                l=mid+1
            