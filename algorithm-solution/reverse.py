#The input is assumed to be a 32-bit signed integer. 
#Your function should return 0 when the reversed integer overflows.

def reverse(self,x): 
        
        flg=0
        
        if x < 0 :
            x= x*-1
            flg=-1
        
        sum=0
        
        while x > 0:
            r= x%10
            x=x/10
            sum = sum * 10 + r      # remember multply by 10
            
        
        
        if flg == -1:
            sum = sum * -1
        
        
        if  sum < -2**31-1 or sum > 2**31 -1:
            return 0
                
        
        
        return sum 


#Explanation :  all 32 bit intergers lie between -2**31 - 1 to 2**31 - 1