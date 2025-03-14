/**
 * @param {string} s
 * @return {string}
 */

var sortSentence = function (s) {
  //   let arr = s.split(" ");
  //   let num = [];
  //   for (let i = 0; i < arr.length; i++) {
  //     num.push(arr[i].charAt(arr[i].length - 1));
  //   }
  //   console.log(num);

  return s
    .split(" ")
    .sort((a, b) => a[a.length - 1] - b[b.length - 1])
    .map((word) => word.slice(0, word.length - 1))
    .join(" ");
};

let s = "is2 sentence4 This1 a3";

console.log(sortSentence(s));
