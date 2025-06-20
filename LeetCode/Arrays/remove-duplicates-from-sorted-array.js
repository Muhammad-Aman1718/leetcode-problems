/**
 * @param {number[]} nums
 * @return {number}
 */

var removeDuplicates = function (nums) {
  let k = 0;

  for (let i = 1; i <= nums.length; i++) {
    if (nums[i] !== nums[i - 1]) {
      nums[k] = nums[i - 1];
      k++;
    }
  }
  return k;

};

let nums = [1, 1, 2];

console.log(removeDuplicates(nums));
