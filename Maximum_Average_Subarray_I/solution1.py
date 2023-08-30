class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        curr = 0
        for n in range(k):
            curr += nums[n]
        ans = curr
            
        for i in range(k, len(nums)):
            #print(i , curr, nums[k-i], nums[i])
            curr = curr + nums[i] - nums[i-k]
            
            ans = max(ans, curr)
            
        #print(curr, ans, k)
        return ans/k