class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # merge the two arrays
        merged = []

        # corner cases
        len_nums1, len_nums2 = len(nums1), len(nums2)

        if len_nums1 == 0: merged = nums2
        elif len_nums2 == 0: merged = nums1
        else:
            # drivers for respective lists
            ptr1 = ptr2 = 0

            while True:
                if nums1[ptr1] < nums2[ptr2]:
                    merged.append(nums1[ptr1])
                    ptr1 += 1 
                
                else: 
                    merged.append(nums2[ptr2])
                    ptr2 += 1

                # if nums1 is exhausted
                if ptr1 == len(nums1):
                    merged = merged + nums2[ptr2:]
                    break
                # if nums2 is exhausted
                elif ptr2 == len(nums2):
                    merged = merged + nums1[ptr1:]
                    break

        len_merged = len(merged)
        m1 = len_merged // 2
        if len_merged % 2 == 0: 
            m2 = m1 - 1
            return (merged[m1] + merged[m2]) / 2
        else:
            return merged[m1]