class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # keeps num: count
        count_dict = {}


        for i in range(len(nums1)):
            # if theres a common number
            if nums1[i] in nums2:
                # capture the count - from array which has fewer duplicates
                count_dict[nums1[i]] = min(nums1.count(nums1[i]), nums2.count(nums1[i])) 

        # list to get the final answer
        answer = []
        for key, value in count_dict.items():
            answer = answer + [key] * value

        return answer