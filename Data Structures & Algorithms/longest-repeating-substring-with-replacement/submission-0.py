class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set()
        maxLength = 0
        for c in s:
            charSet.add(c)
        for c in charSet:
            l = 0
            charCount = 0
            for r in range(len(s)):
                if s[r] == c:
                    charCount += 1
                if ((r-l+1) - charCount) > k:
                    if s[l] == c:
                        charCount -= 1
                    l += 1
                maxLength = max((r-l+1), maxLength)
        return maxLength
        
