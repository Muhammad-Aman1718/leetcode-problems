/**
 * @param {number[]} nums
 * @return {number}
 */

var thirdMax = function (nums) {
  console.log("this is function");

  let uniqueNumbers = [...new Set(nums)];

  uniqueNumbers.sort((a, b) => b - a);
  return nums.length >= 2 ? nums[0] : nums[2];
};

let nums = [3, 2];
// let nums = [1, 2];
// let nums = [2,2,3,1]

console.log(thirdMax(nums));
