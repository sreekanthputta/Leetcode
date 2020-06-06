class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        aCitiesDiff = []
        bCitiesDiff = []
        s = 0
        aCount = 0
        bCount = 0
        for list in costs:
            if(list[0]<list[1]):
                s += list[0]
                aCount+=1
                bCitiesDiff += [list[1]-list[0]]
            else:
                s += list[1]
                bCount+=1
                aCitiesDiff += [list[0]-list[1]]
        aCitiesDiff.sort()
        bCitiesDiff.sort()
        if(aCount<len(costs)/2):
            s += sum(aCitiesDiff[:((int)(len(costs)/2)-aCount)])
        elif(bCount<len(costs)/2):
            s += sum(bCitiesDiff[:((int)(len(costs)/2)-bCount)])
        return s