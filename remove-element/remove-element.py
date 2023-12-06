class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        f_idx = 0
        l_idx = len(nums)-1
        count = 0
        while f_idx<=l_idx:
            if nums[f_idx] == val and nums[l_idx] != val:
                temp = nums[f_idx]
                nums[f_idx] = nums[l_idx]
                nums[l_idx] = temp
                f_idx+=1
                l_idx-=1
                count+=1
            elif nums[f_idx] != val and nums[l_idx] == val:
                f_idx+=1
                l_idx-=1
                count+=1
            elif nums[f_idx] == val and nums[l_idx] == val:
                l_idx-=1
                count+=1
            else: #nums[f_idx] != val and nums[l_idx] != val:
                f_idx+=1
        return(len(nums)-count)