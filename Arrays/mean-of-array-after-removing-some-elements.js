/**
 * @param {number[]} arr
 * @return {number}
 */

var trimMean = function (arr) {
  arr.sort((a, b) => a - b);
  let percentage = Math.floor(arr.length * 0.05);
  let remianingElement = arr.slice(percentage, arr.length - percentage);
  let total = remianingElement.reduce((acc, val) => acc + val, 0);
  let mean = total / remianingElement.length;
  return Number(mean.toFixed(5));
};

// let arr = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3];
// let arr = [6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0];
let arr = [
  6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3,
  8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8, 2, 3, 4,
];
console.log(trimMean(arr));
