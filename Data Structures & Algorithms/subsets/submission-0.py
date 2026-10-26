class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def solve(res,curr,i):
            if i==len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            solve(res,curr,i+1)
            curr.pop()
            solve(res,curr,i+1)

        res=[]
        solve(res,[],0)

        return res
        