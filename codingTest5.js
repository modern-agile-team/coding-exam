const fs = require("fs");
const { kill } = require("process");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution() {
  // 풀이
  const modelNum = input[0].split(" ");
  const brand = {
    삼성: [],
    애플: [],
    hansung: [],
    renover: [],
    lg: [],
    asus: [],
    other: [],
  };

  modelNum.sort((a, b) => a - b);
  for (let n of modelNum) {
    if (1000 <= n && n < 2000) {
      brand.삼성.push(Number(n));
    } else if (2000 <= n && n < 3000) {
      brand.애플.push(Number(n));
    } else if (3000 <= n && n < 4000) {
      brand.hansung.push(Number(n));
    } else if (4000 <= n && n < 5000) {
      brand.renover.push(Number(n));
    } else if (5000 <= n && n < 6000) {
      brand.lg.push(Number(n));
    } else if (6000 <= n && n < 7000) {
      brand.asus.push(Number(n));
    } else {
      brand.other.push(Number(n));
    }
  }
  return brand;
}

console.log(solution());
