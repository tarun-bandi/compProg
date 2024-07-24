class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_nums = []
        i = 0
        for elem in nums:
            map_ele = ""
            for c in str(elem):
                map_ele += str(mapping[int(c)])
            mapped_nums.append((int(map_ele), i, int(elem)))
            i += 1
        print(mapped_nums)
        mapped_nums.sort()
        return list(map(lambda x : x[2], mapped_nums))