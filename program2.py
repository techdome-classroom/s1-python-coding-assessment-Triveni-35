def decode_message( s: str, p: str) -> bool:
        def dfs(i, j):
                if j == len(p):
                        return i == len(s)
                if p[j] == '*':
                        return dfs(i, j+1) or (i < len(s) and dfs(i+1, j))
                if i < len(s) and (p[j] == '?' or s[i] == p[j]):
                        return dfs(i+1, j+1)
                return False
        
        return dfs(0, 0)