class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [n**2 for n in nums]
        if nums[len(nums)-1] <= 0:
            rev = nums[::-1]
            return [n**2 for n in rev]
        
        i=0
        while nums[i]<0:
            i +=1
        
        minus = nums[:i]
        minus = minus[::-1]
        plus = nums[i:]
        
        #print("minus", minus, "plus", plus)
        m=0
        p=0
        ans = []
        while m < len(minus) and p < len(plus):
            if abs(plus[p]) < abs(minus[m]):
                ans.append(plus[p]*plus[p])
                p += 1
            else:
                ans.append(minus[m]*minus[m])
                m += 1
                
                
        while m < len(minus):
            ans.append(minus[m]*minus[m])
            m += 1
            
        while p < len(plus):
            ans.append(plus[p]*plus[p])
            p += 1
            
        return ans

        
        