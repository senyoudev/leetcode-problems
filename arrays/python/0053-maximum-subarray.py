class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=nums[0]
        currentSum=0
        for i in range(len(nums)):
            currentSum+=nums[i]
            if currentSum >= maxSum:
                maxSum = currentSum
            if currentSum<0 :
                currentSum=0
        return maxSum