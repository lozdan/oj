/*
author: Daniel Lozano
source: LeetCode ( https://www.leetcode.com )
problem name: Problems > Validate Binary Search Tree
problem url: https://leetcode.com/problems/validate-binary-search-tree/description/
*/

//Time Complexity: n^2

var isValidBST = function(root) {
    if (!root)
        return true;
    
    let l = isValidBST(root.left);
    let r = isValidBST(root.right);
    
    let checkL = (getMax(root.left) < root.val);
    let checkR = (getMin(root.right) > root.val); 
    
    return (l && r && checkL && checkR);
};


function getMin(root){
    if (!root)
        return 1e11;
    
    let l = getMin(root.left);
    let r = getMin(root.right);
    
    return Math.min(l, r, root.val);
}

function getMax(root){
    if (!root)
        return -1e11;
    
    let l = getMax(root.left);
    let r = getMax(root.right);
    
    return Math.max(l, r, root.val);
}

