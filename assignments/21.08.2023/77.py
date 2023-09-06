class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def dfs(s,temp): 
              if len(temp) == k:
                 ans.append(temp.copy())
                 return

              for i in range(s, n + 1):
                  temp.append(i)
                  dfs(i + 1, temp)
                  temp.pop()

        dfs(1, [])
        return ans