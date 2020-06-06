class Solution:
    
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #people.sort(key = lambda x:x[1])
        #people.sort(key = lambda x:-x[0])
        
        people = sorted(people, key=lambda x: (-x[0], x[1]))

        out = []
        
        for person in people:
            out.insert(person[1] , person)
        return out