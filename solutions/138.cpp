// Title: Copy List with Random Pointer
// Category: Linked List 
// Difficulty: Medium

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
        if (!head) return nullptr;

        std::unordered_map<Node*, Node*> oldToCopy;
        Node* curr = head;

        // First pass: Create all nodes and store them in the map.
        while (curr) { 
            oldToCopy[curr] = new Node(curr->val); 
            curr = curr->next; 
        }

        // Second pass: Assign next and random pointers.
        curr = head;
        while (curr) {
            oldToCopy[curr]->next = oldToCopy[curr->next];
            oldToCopy[curr]->random = oldToCopy[curr->random];
            curr = curr->next;  
        }

        return oldToCopy[head];
    }
};