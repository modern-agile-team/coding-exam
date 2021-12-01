const fs = require("fs");
const { kill } = require("process");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution() {
  const info = input[0].split(" ");
  const result = [];
  const minValue = Math.min.apply(null, info);
  const sumValue = info.reduce((acc, el) => {
    acc += Number(el);
    return acc;
  }, 0);
  const maxValue = Math.max.apply(null, info);

  result.push(minValue);
  result.push(sumValue);
  result.push(maxValue);
  return result;
}

console.log(solution());
