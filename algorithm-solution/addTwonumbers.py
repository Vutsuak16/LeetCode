def addTwoNumbers(l1, l2):
        

        '''I learnt to make it submittable  make sure you know the correct format of the question
        like here reveresed was the format needed, fuck you mathematics knowledge YOU MUST KNOW WHAT THE QUESTION IS 
        asking about'''

        
        k1=""
        k2=""
        while True:
            if l1.next != None:
                k1+=str(l1.val)
                l1=l1.next
            else:
                k1+=str(l1.val)
                break
        
        while True:
            if l2.next != None:
                k2+=str(l2.val)
                l2=l2.next
            else:
                k2+=str(l2.val)
                break
        
                
        l=int(k1[::-1])+int(k2[::-1])
        return map(int,list(str(l))[::-1])