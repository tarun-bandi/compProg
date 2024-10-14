class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        queue = collections.deque([s])

        visited = set()

        while queue:
            word = queue.popleft()

            if word in visited:
                continue
            else:
                if word == "":
                    return True
                
                visited.add(word)
                for start in wordDict:
                    if word.startswith(start):
                        queue.append(word[len(start):])
            
        return False

