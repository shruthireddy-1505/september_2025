class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count=0
        while b!=0:
            temp=a%b
            a=b
            b=temp
        gcd=a
        for i in range(1,int(gcd**0.5)+1):
            if gcd%i==0:
                if i!=gcd//i:
                    count+=2
                else:
                    count+=1
        return count
                