class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in charSet:
                while s[l] != s[r]:
                    charSet.remove(s[l])
                    l+=1
                l+=1
            else:
                charSet.add(s[r])
                res = max(res, len(charSet))
        return res

        # brute force
        # longest = 0
        # for c in s:
        #     freqs = set()
        #     temp = 0
        #     for i in range(s.index(c), len(s)):
        #         if s[i] in freqs:
        #             break
        #         else:
        #             freqs.add(s[i])
        #             temp += 1
        #     if temp > longest:
        #         longest = temp
        # return longest
        
