class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        min_x=min(a,b)
        count=0
        for i in range(1,a+1):
            if a%i==0 and b%i==0:
                count+=1
        return count
        