const fs = require("fs");
const { kill } = require("process");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution() {
  const info = input[0].split(" ");
  const str = [];
  for (let i = 0; i < Number(info[0]); i++) {
    str[i] = info[1];
  }

  return str.join("");
}

console.log(solution());
