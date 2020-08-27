// https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode*> s;
        vector<int> result;

        while(!s.empty() || root){
            if(root){
                s.push(root);
                root = root->left;
            }
            if(!root){
                result.push_back(s.top()->val);
                root = s.top()->right;
                s.pop();
            }
        }
        return result;
    }
};