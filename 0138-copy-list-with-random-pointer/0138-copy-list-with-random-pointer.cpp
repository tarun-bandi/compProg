/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/
#include <unordered_map>

class Solution {
public:
    Node* copyRandomList(Node* head) {
        // First pass: Make a hashmap mapping each node to a copy
        std::unordered_map<Node*, Node*> copies; 

        Node* currentNode = head;
        while (currentNode != NULL){
            Node* copy = new Node(currentNode->val);
            copies[currentNode] = copy;
            currentNode = currentNode->next;
        }

        copies[NULL] = NULL;
        // Second pass: Go through list and connect map[node].next = map[node.next]
        // And same for random

        currentNode = head; 
        while (currentNode != NULL){
            copies[currentNode]->next = copies[currentNode->next];
            copies[currentNode]->random = copies[currentNode->random];
            currentNode = currentNode->next;
        }

        return copies[head];

    }
};