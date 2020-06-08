'''
#Code to find maximum number of coins.
class Solution:
    
    maxCoinsDict = {}
    def change(self, amount: int, coins: List[int]) -> int:
        if(amount in self.maxCoinsDict):
            return self.maxCoinsDict[amount]
        maxCoins = 0
        for coin in coins:
            if amount-coin==0:
                maxCoins = max(1, maxCoins)
            elif amount-coin>0:
                coinsForRemaining = self.change(amount-coin, coins)
                if(coinsForRemaining!=0):
                    maxCoins = max(coinsForRemaining+1, maxCoins)
            print(amount, coin, maxCoins)
        self.maxCoinsDict[amount] = maxCoins
        print(self.maxCoinsDict)
        return maxCoins
'''		
		

#Time limit exceeded
class Solution:    
    waysDict = {}
    def change(self, amount: int, coins: List[int], l=[]) -> int:
        self.waysDict = {}
        if(amount==0):
            return 1
        self.changeRec(amount,coins)
        return len(self.waysDict[amount]) if amount in self.waysDict else 0
    
    def changeRec(self, amount: int, coins: List[int], l=[]) -> int:
        if(amount in self.waysDict):
            for way in self.waysDict[amount]:
                self.appendWay(sum(l) + amount, [int(x) for x in way.split(" ")] + l)
        ways = 0
        for coin in coins:
            if amount-coin==0:
                ways+=1
                #print(l+[coin])
                self.appendWay(sum(l)+amount, l+[coin])
            elif amount-coin>0:
                self.changeRec(amount-coin, coins, l+[coin])
                
        #print(self.waysDict)
        return len(self.waysDict[amount]) if amount in self.waysDict else 0
    
    
    def appendWay(self, amount, appendWays):
        appendWays.sort()
        appendWays = " ".join(str(x) for x in appendWays)
        if(amount in self.waysDict):
            self.waysDict[amount].add(appendWays)
        else:
            self.waysDict[amount] = {appendWays}