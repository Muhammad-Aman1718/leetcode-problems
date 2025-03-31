var sum = function (arr) {
  arr.sort((a, b) => b - a);

  if (arr.length <= 1) {
    return -1;
  } else {
    return arr[1];
  }
};

let arr = [12, 35, 1, 10, 34, 1];
console.log(sum(arr));
