class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in range(0, len(nums)):
            nums[i] = nums[i]*nums[i]
        nums.sort()
            
        return nums
        