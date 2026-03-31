class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        seen = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l in range(len(nums)) and nums[l] == nums[l-1]:
                        l += 1
                        continue
                elif sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
        return res

        # res = []
        # curr = []
        # nums.sort()
        # def dfs(i,curr,total):
        #     if len(curr) == 3 and total == 0:
        #         res.append(curr.copy())
        #         return
        #     elif len(curr) >= 3 or i not in range(len(nums)):
        #         return
            
        #     curr.append(nums[i])
        #     total += nums[i]
        #     dfs(i+1, curr, total)
        #     total -= nums[i]
        #     curr.pop()
        #     j = i + 1
        #     while j in range(len(nums)) and nums[j] == nums[i]:
        #         j += 1
        #     dfs(j, curr, total)
        #     return
            
        # dfs(0,[],0)
        # return res
            
