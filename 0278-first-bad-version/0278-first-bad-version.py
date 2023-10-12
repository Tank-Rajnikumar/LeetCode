# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # for i in range(n):
        #     if isBadVersion(i):
        #         return i
        # return n  
        l,r=1,n
        while l<r:
            mid=l+(r-l)//2
            if isBadVersion(mid):
                r=mid
            else:
                l=mid+1
        return l