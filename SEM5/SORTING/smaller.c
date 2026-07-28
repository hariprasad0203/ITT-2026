class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        smaller_map = {}
        for i, num in enumerate(sorted_nums):
            if num not in smaller_map:
                smaller_map[num] = i
        return [smaller_map[num] for num in nums]

if __name__ == "__main__":
    sol = Solution()
    print(sol.smallerNumbersThanCurrent([8, 1, 2, 2, 3])) 
    print(sol.smallerNumbersThanCurrent([6, 5, 4, 8]))    
