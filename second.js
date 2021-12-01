function Second(number) {
  const min = Math.min.apply(null,number);
  const sum = number.reduce((a,b) => a+b); 
  const max = Math.max.apply(null,number);
  return [min,sum,max];
};
console.log(Second([3]));
