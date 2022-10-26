class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs[0]) == 0: return ""

        ptr = 0
        # let first word be the ref
        ref_word = strs[0]

        while ptr != len(ref_word):

            for index, each_word in enumerate(strs):
                # if any word is ""
                if len(each_word) == 0 or len(each_word) == ptr: return ref_word[0: ptr]

                if each_word[ptr] != ref_word[ptr]:  return ref_word[0: ptr]
            
            ptr += 1

        return ref_word