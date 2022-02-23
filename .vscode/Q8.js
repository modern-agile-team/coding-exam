const result = {};
const data1 = 'woorim 남자';
const data2 = 'soongu 남자';

const splitD1 = data1.split(' ');
const splitD2 = data2.split(' ');

const key = splitD1[0];
const value = splitD1[1];

result.key = value;
console.log(result);