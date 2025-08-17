class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end_of_word = False

class Solution:
    def insert(self, trie: TrieNode, word: str):

        for c in word:
            trie.children[c] = trie.children.get(c, TrieNode())
            trie = trie.children[c]
        trie.end_of_word = True
    
    def find_match_length(self, trie: TrieNode, word: str) -> int:
        length = 0
        for c in word:
            if c in trie.children:
                length += 1
                trie = trie.children[c]
            else:
                return length
        return length

        
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = TrieNode()

        for num in arr1:
            self.insert(root, str(num))
        
        longest_match = 0

        for num in arr2:
            length = self.find_match_length(root, str(num))
            longest_match = max(longest_match, length)
        
        return longest_match
            




        
        