class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        i = 0
        while i<length:
            if arr[i]==0:
                arr.insert(i,0)
                arr.pop()
                i+=1
            i+=1
        return arr