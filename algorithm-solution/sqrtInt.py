 
 #thing I learnt : INTEGERS HAVE BINARY SEARCH PROPERTY AS THEY ARE SORTED
 
 def mySqrt(x):
        
        if x==0: return 0
        if x==1: return 1
        
        start=1
        end=x
        ans=""
        
        while(start<=end):
            
            mid=(start+end) / 2
            
            if mid**2== x:
                return mid
            
            elif mid ** 2 < x:
                
                start=mid+1 #we need floor ans so when square is closer to x we take it 
                ans=mid
            
            else:
                
                end= mid-1
                
        return ans