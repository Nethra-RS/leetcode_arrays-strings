class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        s_count=Counter()
    
        mx=0

        for right in range(len(fruits)):
            s_count[fruits[right]]+=1

            while len(s_count)>2:
                s_count[fruits[left]]-=1
                if s_count[fruits[left]]==0:
                    del s_count[fruits[left]]
                left+=1

            
            mx=max(mx,right-left+1)
        return mx
        


        
      
            

            


        