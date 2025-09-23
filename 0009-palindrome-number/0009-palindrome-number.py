class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        s=0
        if x<0:
            return False
        while x!=0:
            r=x%10
            s=s*10+r
            x//=10
        if temp==s:
            return True
        else:
            return False
        