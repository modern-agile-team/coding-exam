#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main() {
  string input;
  cin >> input;
  istringstream inputStream(input);
  string buf;
  vector<string> timeVec;
  while (getline(inputStream, buf, ':')) {
    timeVec.push_back(buf);
  }
  cout << "[\"" << timeVec.at(0) << "시\", \"" << timeVec.at(1) << "분\", \"" << timeVec.at(2) << "초\"]";
  return 0;
}