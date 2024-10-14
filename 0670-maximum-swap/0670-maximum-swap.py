class Solution:
    def maximumSwap(self, num: int) -> int:
        
        swap_1 = -1
        swap_2 = -1
        largest = -1
        num = list(str(num))
        for i in range(len(num) - 1, -1 ,-1):
            if largest == -1 or num[i] > num[largest]:
                largest = i
            elif num[i] < num[largest]:
                swap_1 = i
                swap_2 = largest
        
        num[swap_1], num[swap_2] = num[swap_2], num[swap_1]
        return int("".join(num))

            





        