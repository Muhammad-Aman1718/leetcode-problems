// Row wise sorting a 2D array

const sorting = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    arr[i].sort((a, b) => a - b);
  }

  return arr;
};

let arr2D = [
  [77, 11, 22, 3],
  [11, 89, 1, 12],
  [32, 11, 56, 7],
  [11, 22, 44, 33],
];
// let length = arr2D.length;
// console.log(length);

console.log(sorting(arr2D));
