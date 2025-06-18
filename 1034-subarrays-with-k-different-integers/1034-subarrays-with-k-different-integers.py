class Solution:
    

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(nums,k):
            left=0
            n_count=Counter()
            res=0

            for right in range(len(nums)):
                n_count[nums[right]]+=1

                while len(n_count)>k:
                    n_count[nums[left]]-=1
                    if n_count[nums[left]]==0:
                        del n_count[nums[left]]
                   
                    left+=1
                res+=right-left+1
            return res
           
        
        return atmost(nums,k)-atmost(nums,k-1)
        
        

        
        

       

            

           
        