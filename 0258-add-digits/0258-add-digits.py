class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            sum_x=0
            temp=num
            while temp!=0:
                r=temp%10
                sum_x+=r
                temp//=10
            num=sum_x
        return num
                