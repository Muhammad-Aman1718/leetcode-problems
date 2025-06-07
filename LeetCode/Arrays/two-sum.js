/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// Using nested / brute force

var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
  return [];
};

//  Using hashMap

var twoSum = function (nums, target) {
  let map = {}; // Store seen numbers and their indices

  for (let i = 0; i < nums.length; i++) {
    let complement = target - nums[i]; // What we need to find
    if (map[complement] !== undefined) {
      return [map[complement], i]; // Return stored index and current index
    }
    map[nums[i]] = i; // Store current number with its index
  }
  return []; // No valid pair found
};

// let number = [3, 2, 9, 5, 5, 4];
let number = [3, 2, 9, 5, 5, 8, 0, 7, 4];
// let target = 9;
let target = 6;

console.log(twoSum(number, target));
