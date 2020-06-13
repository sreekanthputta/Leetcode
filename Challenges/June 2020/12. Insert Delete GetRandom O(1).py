import random
    
class RandomizedSet:

    dsSet = None
    dsList = None
    def __init__(self):
        self.dsDict = {}
        self.dsList = []
        

    def insert(self, val: int) -> bool:
        if(val in self.dsDict):
            return False
        else:
            self.dsList.append(val)
            self.dsDict[val] = len(self.dsList)-1
            return True
        

    def remove(self, val: int) -> bool:
        if(val in self.dsDict):
            self.dsList.remove(val)
            del self.dsDict[val]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        randomNumber = random.randint(0,len(self.dsList)-1)
        return self.dsList[randomNumber]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()