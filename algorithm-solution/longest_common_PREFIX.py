class Solution(object):
    def longestCommonPrefix(self, strs):
        
        k=0
        if len(strs)==0:
            return ""
        elif len(strs)==1:
            return strs[0]
        else:
            prefix=strs[0]
            for i in range(1,len(strs)):
                result=""
                if len(prefix)>len(strs[i]):
                    small=strs[i]
                else:
                    small=prefix
                for j in range(len(small)):
                    if prefix[j]!=strs[i][j]:
                        break
                    else:
                        result+=prefix[j]
                    
                prefix=result
            return prefix