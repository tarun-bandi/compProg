class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

        result = []
        digit2Letters = {2: ["a", "b", "c"], 3: ["d", "e", "f"],
                        4: ["g", "h", "i"], 5: ["j", "k", "l"],
                        6: ["m", 'n', "o"], 7: ["p", "q", "r", "s"],
                        8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}
        def generateall(i, res):
            if i == len(digits):
                if res:
                    result.append(res)
            else:

                for c in digit2Letters[int(digits[i])]:
                    generateall(i + 1, res + c)
            
        generateall(0, "")
        return result