/**
 * @param {number[]} arr
 * @return {boolean}
 */

var canMakeArithmeticProgression = function (arr) {
  //   arr.sort((a, b) => a - b);
  //   let constantNum = arr[1] - arr[0];
  //   for (let i = 2; i < arr.length; i++) {
  //     if (arr[i] - arr[i - 1] !== constantNum) {
  //       return false;
  //     }
  //   }
  //   return true;

  if (arr.length < 2) return true;

  const min = Math.min(...arr);
  const max = Math.max(...arr);
  console.log("this is min : ", min, "max", max);
  const n = arr.length;
  if ((max - min) % (n - 1) !== 0) return false;
  const diff = (max - min) / (n - 1);
  const numSet = new Set(arr);
  for (let i = 0; i < n; i++) {
    if (!numSet.has(min + i * diff)) return false;
  }

  return true;
};

let arr = [3, 5, 1];
// let arr = [1, 2, 4];
console.log(canMakeArithmeticProgression(arr));
