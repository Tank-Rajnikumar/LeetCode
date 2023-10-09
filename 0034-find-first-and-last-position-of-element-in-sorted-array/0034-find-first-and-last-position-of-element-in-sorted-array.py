class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lst=[]
        f1=0
        for i in nums:
            if(i==target):
                f1=1
                lst.append(nums.index(i))
                si=nums.index(i)
                break
        if f1==0:
            return [-1,-1]
        print(lst)
        f1=0
        ns=nums[::-1]
        c=0
        for i in ns:
            if i==target:
                f1=1
                lst.append((len(nums)-c)-1)
                return lst 
            c+=1 
        if f1==0:
            return [-1,-1]