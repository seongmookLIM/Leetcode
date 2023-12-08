class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        length = 1
        left = 0
        # nums = [0,0,1,1,2,3]
        for i in range(1, len(nums)):
            if nums[left] != nums[i]:
                left += 1
                nums[left], nums[i] = nums[i], nums[left]
                length += 1
        
        return length