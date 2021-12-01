const fs = require("fs");
const { kill, prependOnceListener } = require("process");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution() {
  // fs 방식으로 객체를 입력해본적이 없어 테스트를 위해 이렇게 작성했습니다.
  const person = [
    {
      name: "조상우",
      gender: "남자",
      age: 47,
      height: 181,
      weight: 85,
    },
    {
      name: "오일남",
      gender: "남자",
      age: 77,
      height: 175,
      weight: 65,
    },
    {
      name: "한미녀",
      gender: "여자",
      age: 45,
      height: 167,
      weight: 49,
    },
    {
      name: "압둘 알리",
      gender: "남자",
      age: 33,
      height: 172,
      weight: 78,
    },
    {
      name: "장덕수",
      gender: "남자",
      age: 44,
      height: 180,
      weight: 73,
    },
    {
      name: "강새벽",
      gender: "여자",
      age: 27,
      height: 176,
      weight: 54,
    },
  ];
  const people = [];
  /*
  for (let i = 0; i < person.length; i++) {
    if (
      person[i].gender === "남자" &&
      18 < person[i].age &&
      person[i].age < 60 &&
      person[i].weight >= 70 &&
      person[i] >= 170
    ) {
      people.push(person[i].name);
    }
  }
   
  각 객체 안의 값들을 주어진 조건에 맞도록 비교하는 반복을 
  수행한 후 조건에 일치하는 객체의 name을 people에 저장합니다.
  이후 조건에 해당되는 이름이 저장된 people을 리턴해서 출력합니다.
  */

  return people;
}

console.log(solution());
