class Solution:
    def myAtoi(self, str):
        
        if len(str)==0:
            return 0
        
        str=str.strip()
        ct=0
        sign=1
        flg=0
        char='+'
        new=""
        for i in str:
            k=ord(i)-48
            if not(k>=0 and k<=9 ):
                ct+=1
                char=i
            if (k>=0 and k<=9) and ct<=1 and (char=="-" or char=="+"):
                new+=i
                if char=="-":
                    sign=-1
                else:
                    sign=1
            if ct>1:
                break

        if len(new)==0:
                return 0
        else:
            number=0
            ct=0
            for i in new[::-1]:
                k=ord(i)-48
                number+=k*(10**ct)
                ct+=1
            
            print(number)
            if number*sign > 2147483647:
                return 2147483647
            if number*sign<=-2147483648:
                return -2147483648
            return number*sign

        