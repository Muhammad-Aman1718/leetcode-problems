/**
 * @param {number[]} nums
 * @return {number[]}
 */

var sortEvenOdd = function (nums) {
  let duplicateArr = [...nums];

  let evenArr = duplicateArr
    .filter((_, i) => i % 2 === 0)
    .sort((a, b) => a - b);
  let oddArr = duplicateArr.filter((_, i) => i % 2 === 1).sort((a, b) => b - a);

  let evenIndex = 0,
    oddIndex = 0;
  for (let i = 0; i < nums.length; i++) {
    if (i % 2 === 0) {
      duplicateArr[i] = evenArr[evenIndex++];
    } else {
      duplicateArr[i] = oddArr[oddIndex++];
    }
  }

  return duplicateArr;
};

let nums = [4, 1, 2, 3];
console.log(sortEvenOdd(nums));
