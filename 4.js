const fs = require("fs");
const { kill } = require("process");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
function solution() {
  /*
  두개의 문자열을 split을 이용해 분리된 단어를 각각 배열에 저장합니다.
  만들어진 두 개의 배열의 값을 비교하며, 일치할 경우 자릿수를 누적합합니다.
  모든 비교가 끝나면 계산된 누적합을 출력합니다.
  */
}

console.log(solution());
