from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        n=len(nums)
        print(c,n)
        ans=[]
        for i in c.keys():
            if c[i] >= int(n/3)+1:
                ans.append(i)
        return ans