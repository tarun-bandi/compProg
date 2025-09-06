class TrieNode {
public:
    unordered_map<char, shared_ptr<TrieNode>> children;
    bool endOfWord = false;
};

class Trie {
    shared_ptr<TrieNode> root;

public:
    Trie() {
        root = make_shared<TrieNode>();
    }

    void insert(string word) {
        auto cur = root;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                cur->children[c] = make_shared<TrieNode>();
            }
            cur = cur->children[c];
        }
        cur->endOfWord = true;
    }

    bool search(string word) {
        auto cur = root;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                return false;
            }
            cur = cur->children[c];
        }
        return cur->endOfWord;
    }

    bool startsWith(string prefix) {
        auto cur = root;
        for (char c : prefix) {
            if (cur->children.find(c) == cur->children.end()) {
                return false;
            }
            cur = cur->children[c];
        }
        return true;
    }
};