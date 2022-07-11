class Solution:
    def searchInsert(self, nums: list[int], target: int):
        if target in nums:
            return nums.index(target)
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] < target < nums[i+1]:
                return i+1



if __name__ == '__main__':
    nums = [3,5,7,9,10]
    target = 8
    result = Solution().searchInsert(nums, target)
    print(result)
