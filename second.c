#include <stdio.h>

int main() {
  int hours,minutes,seconds;
  scanf("%d:%d:%d",&hours,&minutes,&seconds);//시간,분, 초 입력
  
  if(hours<=24){
  printf("[%d시,",hours);
  }
  if(minutes<=60){
  printf("%d분,",minutes);
  }
  if(seconds<=60){
  printf("%d초]",seconds);
  }
  
  return 0;
}