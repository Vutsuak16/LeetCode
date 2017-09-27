def longestPalindrome(s):
        
        maximum=""
        for i in range(len(s)):
            string=""
            for j in range(i,len(s)):
                string+=s[j] 
                if string==string[::-1]:
                    if len(string)>len(maximum):
                        maximum=string
        
        return maximum




#this is an inefficient solution  was not accepted by Leet Code