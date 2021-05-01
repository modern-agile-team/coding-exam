#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
  int n;
  map<string, string> m;
  cin >> n;
  for (int i = 0; i < n; i++) {
    string name, gender;
    cin >> name >> gender;
    m[name] = gender;
  }
  cout << "{ ";
  for (auto i = m.begin(); i != m.end(); i++) {
    if (i == m.begin()) {
      cout << "\"" << i->first << "\" : \"" << i->second << "\"";
    }
    else {
      cout << ", \"" << i->first << "\" : \"" << i->second << "\"";
    }
  }
  cout << " }";
  return 0;
}