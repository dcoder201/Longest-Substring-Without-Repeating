class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        left, right = 0, 0
        chars = set()
    
        while right < n:
           if s[right] not in chars:
             chars.add(s[right])
             right += 1
             max_len = max(max_len, right - left)
           else:
             chars.remove(s[left])
             left += 1
            
        return max_len
