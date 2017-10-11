def multiply(self, num1, num2):
        
        if len(num1)==1 and len(num2)==1:
            return str(int(num1)*int(num2))
        
        sml=0
        lrg=0
        if len(num1)<len(num2):
            sml=num1
            lrg=num2
        elif len(num1)==len(num2):
            if int(num1[0])>int(num2[0]):
                sml=num2
                lrg=num1
            else:
                sml=num1
                lrg=num2
            
        else:
            sml=num2
            lrg=num1
        
       
        m=[]
        for i in sml[::-1]:
            carry=0
            number=0
            final=""
            ct=0
            for j in lrg[::-1]:
                ct+=1
                a=int(i)*int(j)
                number=carry+a
                carry=number/10
                if ct==len(lrg):
                    final=str(number)+final
                else:
                    final=str(number%10)+final
            
            m.append(final)
        
        s=0
        for i in range(len(m)):
            s+= int(m[i])* (10**i)
        return str(s)