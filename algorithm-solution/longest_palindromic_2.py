def longestPalindrome(s):
        
        memo={}
        maximum=""
        for i in range(len(s)):
            string=""
            for j in range(i,len(s)):
                string+=s[j] 
                if string in memo:
                    if memo[string]>len(maximum):
                        maximum=string
                        continue
                elif string==string[::-1]:
                    memo[string]=len(string)
                    if memo[string]>len(maximum):
                        maximum=string
        
        return maximum



#this a  little bit efficient but even this is not acceptable by leet code
        