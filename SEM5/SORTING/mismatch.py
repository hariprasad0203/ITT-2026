class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        counts = {}
        duplicate = -1
        missing = -1
        for num in nums:
            if num in counts:
                duplicate = num
            counts[num] = counts.get(num, 0) + 1
        for i in range(1, n + 1):
            if i not in counts:
                missing = i
                break
                
        return [duplicate, missing]
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1: {sol.findErrorNums([1,2,2,4])}")
    print(f"Test 2: {sol.findErrorNums([1,1])}") 
