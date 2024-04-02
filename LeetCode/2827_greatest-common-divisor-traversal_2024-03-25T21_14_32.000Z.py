# https://leetcode.com/problems/greatest-common-divisor-traversal

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        MAX_NUM = 100001
        n = len(nums)
        primeLinks = {}
        # numLinks = [[] for _ in range(n)]
        for i in range(n):
            curr = nums[i]
            fac = 2
            while fac * fac <= curr:
                if curr % fac == 0:
                    while curr % fac == 0:
                        curr //= fac
                    # numLinks[i].append(fac)
                    if fac in primeLinks:
                        primeLinks[fac].append(i)
                    else:
                        primeLinks[fac] = [i]
                fac += 1
            if curr > 1:
                if curr in primeLinks:
                    primeLinks[curr].append(i)
                else:
                    primeLinks[curr] = [i]
        print(primeLinks)
        visited = [True] + [False] * (n - 1)
        updated = True
        while updated:
            updated = False
            for fac in primeLinks.keys():
                links = primeLinks[fac]
                if links == None:
                    continue
                connected = False
                for i in links:
                    if visited[i]:
                        connected = True
                if connected:
                    for i in links:
                        visited[i] = True
                    updated = True
                    primeLinks[fac] = None
        for i in range(n):
            if not visited[i]:
                return False
        return True
