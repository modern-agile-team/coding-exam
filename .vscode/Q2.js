const arr = [3, 4];
let result = [];
let sum = 0
arr.forEach((item) => {
    sum += item;
})
result.push(Math.max(...arr));
result.push(sum);
result.push(Math.min(...arr))
console.log(result);