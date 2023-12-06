class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
    
        m_idx = m-1
        n_idx = n-1
        w_idx = m+n-1

        while n_idx>=0:
            if m_idx>=0 and nums1[m_idx] > nums2[n_idx]:
                nums1[w_idx] = nums1[m_idx]
                m_idx -= 1
            else:
                nums1[w_idx] = nums2[n_idx]
                n_idx -= 1
            w_idx -= 1
