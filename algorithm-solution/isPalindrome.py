def isPalindrome(self, x):
        
        sum=0
        temp=x
        
        while x>0:
            r=x%10
            sum=sum*10+r
            x/=10
            
        if sum == temp:
            return True
        else:
            return False