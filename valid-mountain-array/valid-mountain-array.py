class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        max_num = max(arr)
        max_idx = arr.index(max_num)
        if max_idx == 0 or max_idx == len(arr)-1:
            return False
        
        for i in range(0,max_idx):
            if arr[i] >= arr[i+1]:
                return False
        for j in range(max_idx, len(arr)-1):
            if arr[j] <= arr[j + 1]:
                return False
        return True