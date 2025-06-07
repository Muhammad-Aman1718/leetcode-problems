/**
 * @param {number[]} salary
 * @return {number}
 */

var average = function (salary) {
  let minVal = Infinity,
    maxVal = -Infinity,
    total = 0;
  for (let num of salary) {
    if (num < minVal) minVal = num;
    if (num > maxVal) maxVal = num;
    total += num;
  }

  total -= minVal + maxVal;

  // let avg = total / (salary.length - 2);

  return avg;
};

// let salary = [4000, 3000, 1000, 2000];
let salary = [
  25000, 48000, 57000, 86000, 33000, 10000, 42000, 3000, 54000, 29000, 79000,
  40000,
];
console.log(average(salary));
