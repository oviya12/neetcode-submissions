class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(res,open,close,p):
            if open == n and close == n:
                res.append(p)
            if open<n:
                solve(res,open+1,close,p+"(")
            if close<open:
                solve(res,open,close+1,p+")")
        res=[]

        solve(res,0,0,"")

        return res


        