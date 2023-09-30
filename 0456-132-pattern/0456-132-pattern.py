class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if 3 > len(nums):
            return False
            # for i in range(len(nums)-2):
            #     for j in range(i + 1, len(nums) - 1):
            #         for k in range(j + 1, len(nums)):
            #             if nums[i] < nums[k] < nums[j]:
            #                 return True
            #                 exit()
        stack = []
        s3 = float('-inf')

        for num in reversed(nums):
            if num < s3:
                return True 
            while stack and num > stack[-1]:
                s3 = stack.pop()
            stack.append(num)
        return False