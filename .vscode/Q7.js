const str = "13:05:31";
    
const hour = str.slice(0, 2)+"시";
const min = str.slice(3, 5)+"분";
const sec = str.slice(6, 8)+"초";

const arr = [hour, min, sec];
console.log(arr);