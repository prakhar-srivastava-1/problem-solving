class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # sets
        set_note = set(ransomNote)
        set_mag = set(magazine)
        
        # note_dict
        note_dict = {item: ransomNote.count(item) for item in set_note}
        # magazine_dict
        mag_dict = {item: magazine.count(item) for item in set_mag}

        for key, value in note_dict.items():
            try:
                if value > mag_dict[key]:
                    return False
            except KeyError:
                return False
                

        return True