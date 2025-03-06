/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right){
 * this.val = (val=== undefined ? 0 : val)
 * this.left = (left === undefined ? null : left)
 * this.left = (right === undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */

function sortedArrayToBST(nums) {
    // Base case: If the array is empty, return null
    if (nums.length === 0) return null;
  
    // Find the middle element
    const mid = Math.floor(nums.length / 2);
  
    // Create a new TreeNode with the middle element as its value
    const root = {
      value: nums[mid], // Assign the middle value to the root
      left: null,       // Initialize left child as null
      right: null       // Initialize right child as null
    };
  
    // Recursively build the left and right subtrees
    root.left = sortedArrayToBST(nums.slice(0, mid));     // Left subtree: elements before the middle
    root.right = sortedArrayToBST(nums.slice(mid + 1));   // Right subtree: elements after the middle
  
    return root; // Return the root of the BST
  }
  
  const nums = [-10, -3, 0, 5, 9];
  const bst = sortedArrayToBST(nums);
  
  console.log(JSON.stringify(bst, null, 2));
  
