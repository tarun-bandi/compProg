class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        combined_list = []

        for arr in matrix:
            combined_list.extend(arr)
        idx = bisect.bisect_left(combined_list, target) 
        
        return idx < len(combined_list) and combined_list[idx] == target