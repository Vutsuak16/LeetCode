def lengthOfLongestSubstring(self, s):
        if len(s)==0 or len(s)==1:
            return len(s)
        substrings=[]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                substrings.append(s[i:j+1])
            substrings.append(s[i])
        maxi=-1*(2**31-1)
        for i in substrings:
            if len(i)==len(set(i)):
                if len(i)>maxi:
                    maxi=len(i)
        return maxi