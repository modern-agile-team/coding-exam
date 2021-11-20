const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution() {
  // 풀이
  const scores = input[0].split(", ");

  const sum = scores.reduce((acc, el) => {
    acc += Number(el);
    return acc;
  }, 0);

  const avg = Math.round(total / scores.length);
  console.log(avg);
}

console.log(solution());
