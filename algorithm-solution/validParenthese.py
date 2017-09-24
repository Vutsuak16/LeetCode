def isValid(s):
        
        """
        :type s: str
        :rtype: bool
        """
        open=["(","{","["]
        closed=[")","}","]"]
        
        
        stack=[]
        
        if len(s) <=1 or s[0] in closed :
            return  False
        
        for i in s:
            if i in open:
                stack.append(i)
            else:
                if len(stack)==0 and i in closed:
                    return False
                popped=stack.pop()
                if open.index(popped)==closed.index(i):
                    continue
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
            