class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for index, char in enumerate(s):
            if char in s_to_t and s_to_t[char] != t[index]:
                return False

            if t[index] in t_to_s and t_to_s[t[index]] != char:
                return False

            s_to_t[char] = t[index]
            t_to_s[t[index]] = char

        return True