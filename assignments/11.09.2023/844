class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def string1(string):
            ans = []
            for char in string:
                if char != '#':
                    ans.append(char)
                elif ans:
                    ans.pop()
            return ''.join(ans)
        
        return string1(s) == string1(t)