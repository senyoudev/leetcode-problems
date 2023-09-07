class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        result_dict_s = {}
        result_dict_t = {}

        for char in s:
            result_dict_s[char] = result_dict_s.get(char, 0) + 1

        for char in t:
            result_dict_t[char] = result_dict_t.get(char, 0) + 1

        if set(result_dict_s.keys()) == set(result_dict_t.keys()):
            values_are_same = True
    
            for key in result_dict_s.keys():
                if result_dict_s[key] != result_dict_t[key]:
                    values_are_same = False
                    break
    
            return values_are_same
        else:
            return False
        
