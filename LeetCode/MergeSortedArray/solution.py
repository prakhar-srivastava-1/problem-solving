class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        left, right = 0, 0

        if m == 0 and n == 0:
            nums1[:] = []
            return
        
        if m == 0 and n != 0:
            nums1[:] = nums2[:n]
            return

        if m != 0 and n == 0:
            nums1[:] = nums1[:m]
            return

        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]

        while True:
            print(left, right, "||", nums1[left], nums2[right])
            if nums1[left] <= nums2[right]:
                left += 1
            else:
                nums1[:] = nums1[:left] + [nums2[right]] + nums1[left:]
                left += 1
                right += 1
                m += 1
            
            if left >= m:
                nums1[:] = nums1 + nums2[right:]
                break
            if right >= n:
                break