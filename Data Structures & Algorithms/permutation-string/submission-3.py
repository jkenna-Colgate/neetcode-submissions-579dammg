class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)
        for c in s1:
            count[c] += 1
        for l in range(len(s2)):
            if s2[l] in s1 and len(s2) >= l + len(s1):
                temp = count.copy()
                for r in range(l, l + len(s1)):
                    if (s2[r] in s1):
                        temp[s2[r]] -= 1  
                    else:
                        break 
                if (all(value == 0 for value in temp.values())):
                    return True
        return False
                    

