class Solution(object):
    def myPow(self, x, n):
        
        if  n==0 or x==1:
            return 1
        if n==1:
            return x
        if x==0:
            return 0
        if n< 1e-10 and n>0:
            return 0
        if x==-1:
            if n%2==0:
                return 1
            else:
                return -1

        k=1
        if n>0:
            for i in range(n):
                k*=x
                if k< 1e-10 and x>0:
                    return 0
            return k
        else:
            for i in range(-1*n):
                k/=x
                if k<1e-10 and x>0:
                    return 0
                
            return k
            
            
        