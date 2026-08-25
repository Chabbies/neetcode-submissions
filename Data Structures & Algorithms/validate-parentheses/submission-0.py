class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        pairs = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in pairs:
                if check and check[-1] == pairs[c]:
                    check.pop()
                else:
                    return False
            else:
                check.append(c)

        if not check:
            return True
        else:
            return False