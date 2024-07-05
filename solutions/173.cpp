// Title: Binary Search Tree Iterator
// Category: Binary Search tree 
// Difficulty: Medium

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class BSTIterator {
public:
    BSTIterator(TreeNode* root) {
        _leftmost_inorder(root);
    }

    int next() {
        TreeNode* topmost_node = stack.top(); 
        stack.pop(); 

        if ( topmost_node->right ) {
            _leftmost_inorder(topmost_node->right); 
        }

        return topmost_node->val; 
    }

    bool hasNext() {
        return !stack.empty(); 
    }

private: 
    std::stack<TreeNode*> stack; 
    void _leftmost_inorder(TreeNode* root) {
        while ( root ) { 
            stack.push(root); 
            root = root->left; 
        }
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */