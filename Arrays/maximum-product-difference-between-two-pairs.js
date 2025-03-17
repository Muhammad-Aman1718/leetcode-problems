/**
 * @param {number[]} nums
 * @return {number}
 */

var maxProductDifference = function (nums) {
  nums.sort((a, b) => a - b);
  const maxDifference =
    nums[nums.length - 2] * nums[nums.length - 1] - nums[0] * nums[1];
  return maxDifference;
};

let nums = [5, 6, 2, 7, 4];
// let nums = [4, 2, 5, 9, 7, 4, 8];

console.log(maxProductDifference(nums));
