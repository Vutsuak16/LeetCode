def longestPalindrome(self, s):
        
       def longestPalindrome(self, s):
        
        length=len(s)
        
        if length<=1:
            return s
        
        temp=[[False]*length for j in range(length)]
        
        maxlength=1
        i=0
        start=0
        
        for i in range(length):
            temp[i][i]=True                #all strings of length 1 are palindrome
        
        
        for i in range(length-1):
            if s[i]==s[i+1]:
                temp[i][i+1]=True
                maxlength=2
                start=i
        
        for k in range(3,length+1):     #length of the string
            for i in range(length-k+1):      #start index of the string
                j=i+k-1                    #ending index of string 
                if s[i]==s[j] and temp[i+1][j-1]:
                    temp[i][j]=True
                    if k>maxlength:
                        maxlength=k
                        start=i
        
        return s[start:start+maxlength]
                