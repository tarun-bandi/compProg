class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        

        mins = []
        maxs = []
        
        for i, arr in enumerate(arrays):
            inserted = False
            if len(mins) < 2:
                mins.append((arr[0], i))
                inserted = True
                mins.sort()
            if len(maxs) < 2: 
                maxs.append((arr[-1], i))
                inserted = True
                maxs.sort(reverse=True)

            if not inserted:
                current_min = arr[0]
                current_max = arr[-1]

                if current_min < mins[0][0] or current_min < mins[1][0]:
                    mins.pop(-1)
                    mins.append((current_min, i))
                    mins.sort()
                
                if current_max > maxs[0][0] or current_max > maxs[1][0]:
                    maxs.pop(-1)
                    maxs.append((current_max, i))
                    maxs.sort(reverse=True)
        
        print(mins, maxs)
        if mins[0][1] != maxs[0][1]:
            return maxs[0][0] - mins[0][0]
        else:
            return max(maxs[0][0] - mins[1][0], maxs[1][0] - mins[0][0])



            

            
            