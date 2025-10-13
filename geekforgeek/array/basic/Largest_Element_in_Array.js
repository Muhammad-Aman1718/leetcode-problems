// Largest Element in Array

// Given an array arr[]. The task is to find the largest element and return it.

// Examples:

// Input: arr[] = [1, 8, 7, 56, 90]
// Output: 90
// Explanation: The largest element of the given array is 90.
// Input: arr[] = [5, 5, 5, 5]
// Output: 5
// Explanation: The largest element of the given array is 5.
// Input: arr[] = [10]
// Output: 10
// Explanation: There is only one element which is the largest.

class Solution {
  /**
    * @param number[] arr

    * @returns number
    */
  largest(arr) {
    // code here
    // console.log(arr);
    return Math.max(...arr);
  }
}

obj = new Solution();
arr = [1, 8, 7, 56, 90];
console.log(obj.largest(arr));
