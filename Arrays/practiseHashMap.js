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
