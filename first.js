var score = [50, 35, 70 , 50];

var avr = 0;
var sum = 0;
for(let i =0; i<score.length; i++) {
    sum += score[i];
  }
 avr = sum/score.length;

var avrCeil = Math.ceil(avr);
 console.log(avrCeil);


