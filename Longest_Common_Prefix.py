strs = ["flower", "flower", "flower"]


if "" in strs:
    print("")
elif len(strs) <= 1:
    print(strs[0][0])
elif strs.count(strs[0][:]) == len(strs):
    print(strs[0][:])

last = len(strs) - 1
ans = ""
prefix = strs[last][0]
count = 0
run = True

while run:
    for voc in strs:
        if voc[:count+1] != prefix:
            run = False
            print(ans)
            break
    ans = prefix
    count += 1
    prefix = strs[last][:count+1]


# Better solution
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        else:
            l = self.longestCommonPrefix(strs[:len(strs) // 2])
            r = self.longestCommonPrefix(strs[len(strs) // 2:])
            
            p = 0
            while p < len(l) and p < len(r) and l[p] == r[p]:
                p += 1
                
            return l[:p]
"""

