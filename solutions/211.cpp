// Title: Design Add and Search Words Data Structure
// Category: Trie
// Difficulty: Medium 
#include <unordered_map> 
#include <string> 

class WordDictionary {
public:
    struct TrieNode {
        std::unordered_map<char, TrieNode*> children; 
        bool isEndOfWord; 
        TrieNode() : isEndOfWord(false) {}
    };

    TrieNode* root; 

    WordDictionary() {
        root = new TrieNode();      
    }
    
    void addWord(string word) {
        TrieNode* node = root; 
        for ( char ch : word ) {
            if ( node->children.count(ch) == 0 ) { 
                node->children[ch] = new TrieNode(); 
            }
            node = node->children[ch]; 
        }
        node->isEndOfWord = true; 
    }
    
    bool search(string word) {
        return searchHelper(word, 0, root); 
    }

private: 
    bool searchHelper(const std::string& word, int index, TrieNode* node) {
        if ( index == word.size() ) {
            return node->isEndOfWord; 
        }
        char ch = word[index]; 
        if ( ch == '.' ) {
            for ( const auto& child : node->children ) { 
                if ( searchHelper(word, index + 1, child.second) ) {
                    return true; 
                }
            }
            return false; 
        } else { 
            if ( node->children.count(ch) ) {
                return searchHelper(word, index + 1, node->children[ch]);
            } else {
                return false; 
            }
        }
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */