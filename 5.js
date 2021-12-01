const fs = require("fs");
const { kill } = require("process");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution() {
  const pattern = input[0].split("");
  const str = input[1].split(" ");
  const sumStr = [];
  let count = 0;
  for (let i = 0; i < pattern.length; i++) {
    sumStr.push(pattern[i] + str[i]);
  }

  for (let i = 1; i <= pattern.length / 2; i++) {
    if (pattern[i - 1] === pattern[i]) {
      if (sumStr[i - 1] !== sumStr[i]) return false;
    }

    if (sumStr[i - 1] === sumStr[sumStr.length - i]) count += 1;
  }
  return sumStr.length === count;

  /* 
  주어진 패턴을 한 글자씩 배열에 저장합니다 
  다음 문자열을 공백 기준으로 각각 배열에 저장합니다
  이후 첫번째 패턴과 첫번째 문자열을 합쳐 하나의 문자열을 만드는 작업을 반복합니다.
  만들어진 첫번째 문자열과 마지막 문자열을 비교하여 일치하는지 확인하며
  패턴의 길이의 반만큼 반복 비교합니다.
  아무 이상이 없을 경우 true를 반환하며 서로 대응하는 값이 다를 경우 false를 반환합니다.
  */
}

console.log(solution());
