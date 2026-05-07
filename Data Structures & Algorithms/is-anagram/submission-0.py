class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortList1 = []
        sortList2 = []
        for c in s:
            sortList1.append(c)
        for c in t:
            sortList2.append(c)
        sortList1.sort()
        sortList2.sort()
        if sortList1 == sortList2:
            return True
        else:
            return False