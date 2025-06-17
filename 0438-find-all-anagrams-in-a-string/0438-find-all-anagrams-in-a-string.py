from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count=Counter(p)
        s_count=Counter()
        p_len=len(p)
        result=[]

        for i in range(len(s)):

            s_count[s[i]]+=1

            if i>=p_len:
                last_char=s[i-p_len]
                s_count[last_char]-=1
                if s_count[last_char]==0:
                    del s_count[last_char]
                
            if s_count==p_count:
                result.append(i-p_len+1)
        
        return result



        
        