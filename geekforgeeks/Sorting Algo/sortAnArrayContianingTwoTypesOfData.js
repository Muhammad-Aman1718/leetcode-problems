// Sort an array containing two types of elements

const sortingFunc = (arr) => {
  return arr.sort((a, b) => a - b);
};

let arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0];

console.log(sortingFunc(arr));
