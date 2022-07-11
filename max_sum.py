class Solution(object):
    def max_sub_array(self, nums):
        currentSubarray = nums[0]
        maxSubarray = nums[0]
        for i in range(1, len(nums)):
            print(nums[i], currentSubarray + nums[i])
            currentSubarray = max(nums[i], currentSubarray + nums[i])
            maxSubarray = max(maxSubarray, currentSubarray)

        return maxSubarray


if __name__ == '__main__':
    num_list = [1,-7,3,4,1,-10,11]
    result = Solution().max_sub_array(num_list)
    print(result)