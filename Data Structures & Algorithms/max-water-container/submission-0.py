class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAr = 0 
        
        l = 0
        r = len(heights) -1
        while l < r:
            currAr = min(heights[l],heights[r]) * (r - l)
            if currAr > maxAr:
                maxAr = currAr
            if heights[l] > heights[r]:
                r -= 1 
            elif heights[l] < heights[r]:
                l += 1    
            elif heights[l] == heights[r]: 
                l += 1
            
        return maxAr


        