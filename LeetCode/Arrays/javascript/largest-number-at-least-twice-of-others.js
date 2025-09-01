/**
 * @param {number[]} nums
 * @return {number}
 */

var dominantIndex = function (nums) {
  let orignalArr = [...nums];
  nums.sort((a, b) => a - b);

  let big = nums[nums.length - 2] + nums[nums.length - 2];
  if (big <= nums[nums.length - 1]) {
    for (const i in orignalArr) {
      if (nums[nums.length - 1] === orignalArr[i]) {
        return Number(i);
      }
    }
  } else {
    return -1;
  }
};

let nums = [3, 6, 1, 0];
// let nums = [1, 2, 3, 4];

console.log(dominantIndex(nums));