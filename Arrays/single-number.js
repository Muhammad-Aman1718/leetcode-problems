/**
 * @param {number[]} nums
 * @return {number}
 */

var singleNumber = function (nums) {
  let number = 0;
  for (let i = 0; i < nums.length; i++) {
    for (let j = 1; j < nums.length; j++) {
      // if (nums[i] !== nums[j]) {
      //   console.log(nums[i]);
      //   number++;
      // } else {
      //   break;
      // }
    }
  }
  return number;
};

let nums = [2, 2, 1];
console.log(singleNumber(nums));
