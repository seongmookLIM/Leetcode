class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = nums[0]
        max2 = float('-inf')
        max3 = float('-inf')

        if len(nums)<3:
            return max(nums)
            

        for i in range(len(nums)):
            num = nums[i]

            if(num>max1):
                max3 = max2
                max2 = max1
                max1 = nums[i]

            elif(num>max2 and num<max1):
                max3 = max2
                max2 = num

            elif(num>max3 and num<max2):
                max3 = num

        if max3 != float('-inf'):
            return max3
        else:
            return max1