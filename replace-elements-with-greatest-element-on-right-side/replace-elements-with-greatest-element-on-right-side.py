class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_val = -1
        for i in range(len(arr)-1, -1, -1):
            temp = max_val
            max_val = max(max_val, arr[i])
            arr[i] = temp
        return arr