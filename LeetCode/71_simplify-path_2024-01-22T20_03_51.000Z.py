# https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        canonical_dirs = []
        for dir in dirs:
            if dir == ".":
                continue
            elif dir == "..":
                if canonical_dirs:
                    canonical_dirs.pop()
                continue
            elif dir == "":
                continue
            canonical_dirs.append(dir)
        rslt = ""
        if not canonical_dirs:
            canonical_dirs.append("")
        for dir in canonical_dirs:
            rslt = rslt + "/" + dir
        return rslt
        