// const insertionSort = (arr) => {
//   for (let i = 1; i < arr.length; i++) {
//     let curr = arr[i];
//     let prev = i - 1;
//     console.log("this is prev 1 : ", prev);

//     while (prev >= 0 && arr[prev] > curr) {
//       arr[prev + 1] = arr[prev];
//       prev--;
//       console.log("this is prev 2 : ", prev);
//       console.log("this is prev 2 : ", arr);
//     }
//     console.log("this is prev 3: ", prev);
//     arr[prev + 1] = curr;
//   }
//   return arr;
// };

// const arr = [3, 4, 1, 8, 2, 6];
// console.log(insertionSort(arr));

// Convert to any decimal number into binary form

// const decimalConverter = (num) => {
//   const arr = [];

//   while (num > 0) {
//     arr.unshift(num % 2);

//     let binary = num / 2;
//     num = ~~binary;
//   }
//   return arr.join(" ");
// };

// const num = 5;
// console.log(decimalConverter(num));

const insertionSort = (arr, n) => {
  for (let i = 1; i < n; i++) {
    let curr = arr[i];
    let prev = i - 1;

    while (prev >= 0 && arr[prev] > curr) {
      arr[prev + 1] = arr[prev];
      prev--;
      console.log(arr);
    }

    arr[prev + 1] = curr;
  }
  console.log(arr);
};

let arr = [31, 41, 59, 26, 41, 58];
let num = 6;

insertionSort(arr, num);
