def countAndSay( n):
        
        if n==1 : return "1"
        if n==2 : return  "11"
        sol="11"
        for i in range(3,n+1):    
            sol+="X"
            ct=1
            temp=""
            for j in range(1,len(sol)):
                if sol[j] != sol[j-1]:
                    temp+=str(ct)
                    temp+=sol[j-1]
                    ct=1

                else: ct+=1

            sol=temp       

            
        return sol