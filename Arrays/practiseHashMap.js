// function bubbleSort(arr) {
//   let n = arr.length;
//   for (let i = 0; i < n - 1; i++) {
//     for (let j = 0; j < n - i - 1; j++) {
//       if (arr[j] > arr[j + 1]) {
//         [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]; // Swap
//       }
//     }
//   }
//   return arr;
// }

// function selectionSort(arr) {
//   let n = arr.length;
//   for (let i = 0; i < n; i++) {
//     let minIdx = i;
//     for (let j = i + 1; j < n; j++) {
//       if (arr[j] < arr[minIdx]) minIdx = j;
//     }
//     [arr[i], arr[minIdx]] = [arr[minIdx], arr[i]]; // Swap
//   }
//   return arr;
// }

// function insertionSort(arr) {
//   let n = arr.length;
//   for (let i = 1; i < n; i++) {
//     let key = arr[i],
//       j = i - 1;
//     while (j >= 0 && arr[j] > key) {
//       arr[j + 1] = arr[j];
//       j--;
//     }
//     arr[j + 1] = key;
//   }
//   return arr;
// }

// function mergeSort(arr) {
//   if (arr.length <= 1) return arr;
//   let mid = Math.floor(arr.length / 2);
//   let left = mergeSort(arr.slice(0, mid));
//   let right = mergeSort(arr.slice(mid));

//   return merge(left, right);
// }

// function merge(left, right) {
//   let result = [],
//     i = 0,
//     j = 0;
//   while (i < left.length && j < right.length) {
//     result.push(left[i] < right[j] ? left[i++] : right[j++]);
//   }
//   return result.concat(left.slice(i)).concat(right.slice(j));
// }

// function quickSort(arr) {
//   if (arr.length <= 1) return arr;
//   let pivot = arr[arr.length - 1];
//   let left = arr.filter((el) => el < pivot);
//   let right = arr.filter((el) => el > pivot);
//   let middle = arr.filter((el) => el === pivot);
//   return [...quickSort(left), ...middle, ...quickSort(right)];
// }

// // Test Array
// let testArray = [64, 25, 12, 22, 11];

// console.log("Bubble Sort:", bubbleSort([...testArray]));
// console.log("Selection Sort:", selectionSort([...testArray]));
// console.log("Insertion Sort:", insertionSort([...testArray]));
// console.log("Merge Sort:", mergeSort([...testArray]));
// console.log("Quick Sort:", quickSort([...testArray]));

// function bigSorting(unsorted) {
//   return unsorted.sort((a, b) => {
//     // Compare by length first
//     if (a.length !== b.length) {
//       return a.length - b.length;
//     }
//     // If same length, compare as strings (lexicographically)
//     return   a > b ? 1 : -1;
//   }); // Convert to number and sort
// }

// // Example Usage
// let testArray = ["64", "25", "12", "22", "11"];
// console.log(bigSorting(testArray)); // Output: [11, 12, 22, 25, 64]

// function sorting(arr) {
//   let n = arr.length;
//   for (let i = 0; i < n - 1; i++) {
//     // console.log(arr[i]);
//     for (let j = 0; j < n - i - 1; j++) {
//       if (arr[j] > arr[j + 1]) {
//         [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
//       }
//     }
//   }
//   return arr;
// }

// let arr = [5, 3, 8, 1, 2];
// // let arr = ["3", "100", "20", "1"];
// console.log(sorting(arr));

function insertionSort1(n, arr) {
  // Write your code here
  key = arr[n - 1];
  i = arr[n - 2];

  while (i >= 0 && arr[i] > key) {
    arr[i + 1] = arr[i]; 
    console.log(arr.join(" ")); 
    i--;
  }

  arr[i + 1] = key;
  console.log(arr.join(" "));
}

let int = 5;
let arr = [1, 2, 4, 5, 3];

console.log(insertionSort1(int, arr));
