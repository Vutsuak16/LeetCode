class Solution(object):
    def letterCombinations(self, digits):
        l={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        
        digits=digits.replace("1","").replace("0","")
        if digits.strip()=="":
            return []
        result=[""]
        for i in digits:
            letters=l[i]
            result=[prefix+letter for prefix in result for letter in letters]
        return result
        