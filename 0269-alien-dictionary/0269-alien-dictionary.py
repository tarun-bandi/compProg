class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        letters = set()
        for c in words[-1]:
            letters.add(c)
        for i, word in enumerate(words[:-1]):
            # edge to first letter of word next to it
            for c in word:
                letters.add(c)
            next_word = words[i+1]
            
            j = 0

            while j < len(next_word) and j < len(word) and word[j] == next_word[j]:
                j += 1
            
            if len(next_word) < len(word) and j == len(next_word):
                return ""
            if j < len(next_word) and j < len(word):
                graph[word[j]].add(next_word[j])
        
        in_degree = defaultdict(int)
        for c, nei in graph.items():
            for char in nei:
                in_degree[char] += 1
        
        print(graph, in_degree, letters)
        queue = deque()

        for c in letters:
            if in_degree[c] == 0:
                queue.append(c)
        
        result = []
        while queue:
            curr = queue.popleft()
            result.append(curr)

            for nei in graph[curr]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        return ''.join(result) if len(result) == len(letters) else ""
