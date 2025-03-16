/**
 * @param {string} s
 * @return {string}
 */

var sortSentence = function (s) {
  return s
    .split(" ")
    .sort((a, b) => a[a.length - 1] - b[b.length - 1])
    .map((word) => word.slice(0, word.length - 1))
    .join(" ");
};

let s = "is2 sentence4 This1 a3";
// let s = "my3 you1 hero4 are2";

console.log(sortSentence(s));
