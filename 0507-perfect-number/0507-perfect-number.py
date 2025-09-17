class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum_x=0
        for i in range(1,int(num**0.5)+1):
            if num%i==0:
                if i!=num//i:
                    sum_x+=i+(num//i)
                else:
                    sum_x+=i
        if (sum_x-num)==num:
            return True
        else:
            return False
                