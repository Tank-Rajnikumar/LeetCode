class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)//2):
        #     for odd in range(1,len(nums)-2,2):
        #         if nums[odd] < nums[odd+2]:
        #             temp=nums[odd]
        #             nums[odd]=nums[odd+2]
        #             nums[odd+2]=temp
        # for i in range(len(nums)//2):
        #     for even in range(0,len(nums)-2,2):
        #         if nums[even] > nums[even+2]:
        #             temp=nums[even]
        #             nums[even]=nums[even+2]
        #             nums[even+2]=temp
        # return nums
        nums[::2],nums[1::2]=sorted(nums[::2]),sorted(nums[1::2],reverse=True)
        return nums