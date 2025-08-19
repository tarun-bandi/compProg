class TrieNode:
    def __init__(self):
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

    
    def find_prefix_len(self, word):

        length = 0
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
                length += 1
            else:
                break

        return length
            



class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = Trie()
        prefix_len = 0 
        for word in arr1:
            root.insert(str(word))
        
        for word in arr2:
            prefix_len = max(prefix_len, root.find_prefix_len(str(word)))
        
        return prefix_len

        