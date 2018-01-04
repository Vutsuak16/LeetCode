class Solution(object):
    def groupAnagrams(self, strs):
        
    
        l=strs
        l=map(sorted,l)
        k=[]
        h={}
        
        k=list(map(lambda x : "".join(x),l))
        
        for i in range(len(k)):
            d=[]
            if k[i] not in h.keys():
                d.append(strs[i])
            for j in range(i+1,len(k)):
                if k[i]==k[j] and k[i] not in h.keys():
                    d.append(strs[j])
            if len(d)!=0:
                h[k[i]]=d
            
        return h.values()