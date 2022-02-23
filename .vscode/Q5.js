const N = 'abba';
const M = 'foo bar bar foo';

const arr1 = N.split();
const arr2 = M.split(' ');
for(let i = 0; i < arr1.length; i++) {
    if (arr1[i] === arr2[i]) {
        console.log(true);
    } else {
        console.log(false);
    }
}