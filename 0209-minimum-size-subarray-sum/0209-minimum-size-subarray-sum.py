class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        window_sum=0
        min_len=float('inf')

        for right in range(len(nums)):
            window_sum+= nums[right]

            while window_sum>=target:
                window_sum-=nums[left]
                min_len=min(min_len,right-left+1)
                left+=1

        if min_len==float('inf'):
            return 0
        else:
            return min_len



        