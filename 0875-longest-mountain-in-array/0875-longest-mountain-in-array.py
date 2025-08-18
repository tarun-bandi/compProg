class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        peaks = []

        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                peaks.append(i)
            
        longest_mountain = 0
        for peak in peaks:
            right_end = peak
            while right_end < len(arr) - 1:
                if arr[right_end] > arr[right_end + 1]:
                    right_end += 1
                else:
                    break
            left_end = peak
            while left_end > 0:
                if arr[left_end] > arr[left_end - 1]:
                    left_end -= 1
                else:
                    break
            longest_mountain = max(longest_mountain, right_end - left_end + 1)
        
        return longest_mountain


