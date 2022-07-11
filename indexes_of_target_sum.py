class Solution:
    def twoSum(self, nums: list[int], target: int):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i !=j:
                    if nums[i] + nums[j] == target:
                        return [i, j]


if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    result = Solution().twoSum(nums, target)
    print(result)