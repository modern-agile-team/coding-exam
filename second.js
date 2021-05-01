let time ="13:52:03";
let timeArr = ["Ω√", "∫–", "√ "];
let splits = time.split(':');
let i =0;
let answer = [];

for(let i=0; i<splits.length; i++) {
   answer.push(splits[i] + timeArr[i]);
}
console.log(answer);
