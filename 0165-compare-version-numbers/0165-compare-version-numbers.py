class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        v1_list = version1.split(".")
        v2_list = version2.split(".")
        index = 0
        v1_list = list(map(float, v1_list))
        v2_list = list(map(float, v2_list))
        while index < min(len(v1_list), len(v2_list)):
            print(v1_list[index], v2_list[index])
            if v1_list[index] < v2_list[index]:
                return -1
            if v2_list[index] < v1_list[index]:
                return 1
            index += 1
        if len(v1_list) < len(v2_list):
            while index != len(v2_list):
                if v2_list[index] != 0.0:
                    return -1
                index += 1
        elif len(v1_list) > len(v2_list):
            while index != len(v1_list):
                if v1_list[index] != 0.0:
                    return 1
                index += 1
        return 0

        