class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        graph = defaultdict(set)
        
        for account in accounts:
            for i in range(1, len(account)):
                for k in (account[1:i] + account[i+1:]):
                    graph[account[i]].add(k)

        seen = set()
        def dfs(node, accts):
            seen.add(node)
            accts.append(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor, accts)
        
        total = []
        for account in accounts:
            res = []
            if account[1] not in seen:
                dfs(account[1], res)
                total.append([account[0]] + sorted(res))
        return total

