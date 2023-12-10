class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = []
        k = 0

        for i in range(0, len(heights)):
            expected.append(heights[i])

        expected.sort()

        for i in range(0, len(heights)):
            if heights[i] != expected[i]:
                k+=1

        return k