class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        out=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        o=0
        e=0
        for i in range(len(nums)):
            if i%2==0:
                if(len(even)>e):
                    out.append(even[e])
                    e+=1
            else:
                if(len(odd)>o):
                    out.append(odd[o])
                    o+=1
        return out