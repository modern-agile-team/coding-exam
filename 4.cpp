#include <iostream>
#include <string>

using namespace std;

string lowerUpperUpperLower(string s) {
  string result = "";
  for (int i = 0; i < (s.size() / 2); i++) {
    char c = s.at(i);
    if (c >= 65 && c <= 90) result += (c + 32);
    else if (c >= 97 && c <= 122) result += (c - 32);
    else result += c;
  }
  return result;
}

void f(string s) {
  cout << s << endl;
  if (s.empty() == false && s.at(0) == ' ') s.erase(0, 1);
  if (s.empty()) return;
  for (int i = 1; i < s.size(); i++) {
    int j;
    for (j = 0; j <= i; j++) {
      if (s.at(j) != s.at(j + i + 1)) break;
    }
    if (j == i + 1) {
      //cout << lowerUpperUpperLower(s.substr(0, i * 2 + 2)) << ' ';
      if (s.size() < i * 2 + 2) s.clear();
      else s.erase(0, i * 2 + 2);
      break;
    }
  }
  return f(s);
}

int main() {
  string input;
  getline(cin, input);
  f(input);
  return 0;
}