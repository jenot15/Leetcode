class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k-1 
        suma = sum(nums[left:right+1])
        ans = suma/k
        
        #print(ans, suma)
        
        for right in range(k-1, len(nums)-1):
            
            if (right-left+1) == k:
                #ans = max(ans, sum(nums[left:right+1])/k)
                suma = suma - nums[left] + nums[right+1]
                ans = max(ans, suma/k)
            #print(left, right, ans,suma,nums[left],nums[right+1], nums[left:right+1])    
            left += 1
               
                
        return ans