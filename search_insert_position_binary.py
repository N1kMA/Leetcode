class Solution:
    def searchInsert(self, nums: list[int], target: int):
        left, right = 0, len(nums) - 1
        if nums[0] > target:
            return 0
        if nums[len(nums)-1] < target:
            return len(nums)
        if target in nums:
            return nums.index(target)
        while left <= right:
            middle = (left + right) // 2
            middle_value = nums[middle]
            if middle_value > target:
                right = middle - 1
            if middle_value < target:
                left = middle + 1
        return left


if __name__ == '__main__':
    nums = [1, 3, 5, 6, 9]
    target = 2
    result = Solution().searchInsert(nums, target)
    print(result)
