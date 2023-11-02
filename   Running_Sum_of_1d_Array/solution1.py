class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i]+prefix[-1])
        
        minimum = min(prefix)
        #print(minimum, abs(minimum - 1))
        
        if minimum == 1:
            return 1
        
        return abs(minimum - 1)
            
        