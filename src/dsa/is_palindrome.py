class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        clean_s = ''.join(ch for ch in s if ch.isalnum())
        l = 0
        r = len(clean_s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True



s=".,a!!"
o = Solution()
print(o.isPalindrome(s))
