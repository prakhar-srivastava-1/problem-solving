class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # approach
        # hold the last seen element
        # keep a ptr to nums array
        # if last seen and current num are different
        # update num at ptr and increment it by 1
        # update last seen

        # corner case
        if len(nums) == 1: return 1
        
        # hold the last seen
        last_seen = nums[0]

        # ptr to hold location where update has to be made
        ptr = 1
        
        for index, item in enumerate(nums):
            if last_seen == item:
                continue
            else:
                nums[ptr] = item 
                last_seen = item
                ptr += 1

        return ptr