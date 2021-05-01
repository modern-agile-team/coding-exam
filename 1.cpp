#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
  string input;
  getline(cin, input);
  istringstream inputStream(input);
  string buf;
  int sum = 0;
  int cnt = 0;
  while (getline(inputStream, buf, ',')) {
    cnt += 1;
    sum += stoi(buf);
  }
  cout << (int)round(sum / (double)cnt);
  return 0;
}