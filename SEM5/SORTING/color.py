class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero_count = 0
        one_count = 0
        
        for num in nums:
            if num == 0:
                zero_count += 1
            elif num == 1:
                one_count += 1


        for i in range(len(nums)):
            if i < zero_count:
                nums[i] = 0
            elif i < zero_count + one_count:
                nums[i] = 1
            else:
                nums[i] = 2
