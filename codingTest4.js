const fs = require("fs");
const { kill } = require("process");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution() {
  // 풀이
  const wrongWords = input[0].split(" ");
  const rightWords = [];

  for (let word of wrongWords) {
    for (z = 1; z <= word.length / 2; z++) {
      if (word.slice(0, z) === word.slice(word.length - z)) {
        word = word.substring(0, z);
        rightWords.push(convertToUpAndLower(word));
      }
    }
  }
  return rightWords.join(" ");
}

function convertToUpAndLower(word) {
  let s = "";
  for (let w of word) {
    s += isUpper(w) ? w.toLowerCase() : w.toUpperCase();
  }
  return s;
}

function isUpper(w) {
  return w === w.toUpperCase();
}

console.log(solution());
