/**
 * @param {number[]} arr
 * @return {number[][]}
 */

var minimumAbsDifference = function (arr) {
  arr.sort((a, b) => a - b);
  console.log("this is Arr", arr);
  let newArr = [];
  let num = 1;
  let diffArr = [];

  for (let i = 0; i < arr.length; i++) {
    diffArr.push(arr[num] - arr[i]);
    num++;
  }
  diffArr.pop();
  diffArr.sort((a, b) => a - b);
  let num2 = 1;
  for (let i = 0; i < arr.length; i++) {
    diffArr.push(arr[num2] - arr[i]);
    if (arr[num2] - arr[i] === diffArr[0]) {
      newArr.push([arr[i], arr[num2]]);
    }
    num2++;
  }

  return newArr;
};

// let arr = [4, 2, 1, 3];
// let arr = [1,3,6,10,15]
// let arr = [3, 8, -10, 23, 19, -4, -14, 27];
let arr = [40, 11, 26, 27, -20];

console.log(minimumAbsDifference(arr));
