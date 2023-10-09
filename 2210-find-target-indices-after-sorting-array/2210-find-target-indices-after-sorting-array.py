class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output=[]
        n=sorted(nums)
        for i in range(len(n)):
            if n[i]==target:
                output.append(i)
        return output