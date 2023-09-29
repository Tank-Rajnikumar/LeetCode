class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # perv=0
        # flag1=1
        # for i in range(len(nums)-1):
        #     if not nums[i] <= nums[i+1]:
        #         flag1=0
        # flag2=1
        # for i in range(len(nums)-1):
        #     if not nums[i] >= nums[i+1]:
        #         flag2=0
        # if flag1 or flag2:
        #     return True
        # else:
        #     return False
        return all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) or all(nums[j] >= nums[j+1] for j in range(len(nums)-1))