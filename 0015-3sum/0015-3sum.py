class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # lst=[]
        # nums=sorted(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         for k in range(len(nums)):
        #             if i !=j and i != k and j != k and nums[i]+nums[j]+nums[k] == 0:
        #                     lst.append(sorted([nums[i],nums[j],nums[k]]))
        #                     continue
        # lst2=[]
        # for i in lst:
        #     if i not in lst2:
        #         lst2.append(i)
        # return lst2
        nums = sorted(nums)
        result = set()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate values

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicate values
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicate values
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return [list(triplet) for triplet in result]
