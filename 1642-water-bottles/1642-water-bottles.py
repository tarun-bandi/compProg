class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalDrank = 0
        leftovers = 0
        while numBottles != 0:
            print(numBottles, leftovers)
            totalDrank += numBottles
            oldBottles = numBottles
            numBottles = (numBottles + leftovers) //numExchange
            leftovers = (oldBottles + leftovers) % numExchange
        return totalDrank
