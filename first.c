#include <stdio.h>

int main() {
  int score, n, average;
  double sum;

  n=0;
  sum=0;  //변수 초기화
  score=0;

  printf("점수를 입력하세요\n종료하려면 음수나 100이 넘는 수를 입력하세요\n");
  while(score>=0&&score<=100)//점수가 0보다 크고, 100보다 작을때
  {
    scanf("%d, ",&score);
    sum += score;
    n++;
  }

  sum= sum - score;
  n--;

  average = sum / n;
  printf("평균은 %d입니다.",average);
  return 0;
}