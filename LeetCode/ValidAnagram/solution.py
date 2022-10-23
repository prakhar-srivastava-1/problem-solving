class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if lengths are unequal => return False
        if len(s) != len(t): return False

        # if there is a mismatch of distinct characters => return False
        set_s, set_t = set(s), set(t)
        if set_s != set_t: return False

        # use hashmap
        # item: count
        s_dict = {item: s.count(item) for item in set_s}

        # get count of other set t
        t_dict = {item: t.count(item) for item in set_t}

        for key, value in s_dict.items():
            if t_dict[key] == value:
                continue
            else:
                return False
        
        return True
