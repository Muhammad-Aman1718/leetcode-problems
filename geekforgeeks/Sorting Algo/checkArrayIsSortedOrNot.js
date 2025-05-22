// JavaScript program Iterative approach to check if an
// Array is sorted or not

// Function that returns true if array is
// sorted in non-decreasing order.
function arraySortedOrNot(arr, n) {
  if (n == 0 || n == 1) {
    return true;
  }

  for (let i = 1; i < n; i++) {
    if (arr[i - 1] > arr[i]) {
      return false;
    }
  }

  return true;
}

// Driver Code
let arr = [20, 23, 23, 45, 78, 88];
let n = arr.length;

if (arraySortedOrNot(arr, n)) {
  console.log("Yes");
} else {
  console.log("No");
}
