const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution() {
  // 풀이
  const time = input[0].split(":");
  return [`${time[0]}시`, `${time[1]}분`, `${time[2]}초`];
}

console.log(solution());
