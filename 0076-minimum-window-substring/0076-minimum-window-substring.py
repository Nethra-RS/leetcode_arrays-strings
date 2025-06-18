class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        s_count = defaultdict(int)

        required = len(t_count)  
        formed = 0 

        left = 0
        min_len = float('inf')
        min_start = 0

        for right in range(len(s)):
            char = s[right]
            s_count[char] += 1

            if char in t_count and s_count[char] == t_count[char]:
                formed += 1

         
            while formed == required:
               
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

               
                s_count[s[left]] -= 1
                if s[left] in t_count and s_count[s[left]] < t_count[s[left]]:
                    formed -= 1
                left += 1

        if min_len == float('inf'):
            return ""
        return s[min_start:min_start + min_len]


            

