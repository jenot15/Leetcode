class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [0,nums[0]]
        l = len(nums)
        for n in range(1, l):
            prefix.append(nums[n] + prefix[-1])
        ans =[]
        double_k = (2*k) + 1
        #print(prefix)
        for i in range(l):
            if (i<k) or i >= (l-k):
                ans.append(-1)
            else:
                #print(k, i, prefix[i+k+1], prefix[i-k])
                ans.append((prefix[i+k+1]-prefix[i-k])//double_k)
        return ans
        