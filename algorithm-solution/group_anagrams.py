class Solution(object):
    def groupAnagrams(self, strs):
        
    
        sortedwords={}
        
        for i in strs:
            
            sortedword=str(sorted(i))
            sortedwords[sortedword]=[i] if sortedword not in sortedwords else sortedwords[sortedword]+[i]
        
            
        return sortedwords.values()
                    
                    
                        
                    
            
                
            
                           
        