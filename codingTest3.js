const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const people = {};

let [typingCount, maxTypingCount] = [0, 0];
let isNumber = true;

rl.on("line", (input) => {
  if (isNumber) {
    maxTypingCount = Number(input);
    isNumber = false;
    return;
  }
  typingCount += 1;

  person = input.split(" ");
  people[person[0]] = person[1];

  if (maxTypingCount === typingCount) rl.close();
});
rl.on("close", () => {
  console.log(people);
});
