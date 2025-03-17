/**
 * @param {number[]} nums
 * @return {number}
 */

var findNonMinOrMax = function (nums) {
  nums.sort((a, b) => a - b);
  if (nums.length <= 2) {
    return -1;
  } else {
    return nums[1];
  }

  //   return maxDifference;
};

let nums = [2, 1, 3];
// let nums = [4, 2, 5, 9, 7, 4, 8];

console.log(findNonMinOrMax(nums));
