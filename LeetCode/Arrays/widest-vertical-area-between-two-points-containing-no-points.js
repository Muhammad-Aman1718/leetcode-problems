/**
 * @param {number[][]} points
 * @return {number}
 */

var maxWidthOfVerticalArea = function (points) {
  let firstElement = points.map((a) => a[0]);
  firstElement.sort((a, b) => a - b);
  console.log(firstElement);
  let differences = firstElement
    .slice(1)
    .map((acc, curr) => Math.abs(firstElement[curr] - acc));

  return Math.max(...differences);
};

// let points = [
//   [8, 7],
//   [9, 9],
//   [7, 4],
//   [9, 7],
// ];

let points = [
  [3, 1],
  [9, 0],
  [1, 0],
  [1, 4],
  [5, 3],
  [8, 8],
];

console.log(maxWidthOfVerticalArea(points));
