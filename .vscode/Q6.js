const str = "50, 100, 50, 75"
let sum = 0;

const arr = str.split(', ');
arr.forEach((i) => {
    sum +=  Number(i)
})
console.log(Math.round(sum/arr.length));
