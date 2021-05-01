#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  map<string, vector<int>> m;
  m["삼성"] = {  };
  m["애플"] = {  };
  m["한성"] = {  };
  m["레노버"] = {  };
  m["LG"] = {  };
  m["아수스"] = {  };
  m["기타"] = {  };
  string input;
  getline(cin, input);
  istringstream inputStream(input);
  string buf;
  while (getline(inputStream, buf, ' ')) {
    int num = stoi(buf);
    if (num >= 7000) {
      m["기타"].push_back(num);
    }
    else if (num >= 6000) {
      m["아수스"].push_back(num);
    }
    else if (num >= 5000) {
      m["엘지"].push_back(num);
    }
    else if (num >= 4000) {
      m["레노버"].push_back(num);
    }
    else if (num >= 3000) {
      m["한성"].push_back(num);
    }
    else if (num >= 2000) {
      m["애플"].push_back(num);
    }
    else if (num >= 1000) {
      m["삼성"].push_back(num);
    }
    else {
      m["기타"].push_back(num);
    }
  }
  cout << "{" << endl;
  for (auto i: m) {
    sort(i.second.begin(), i.second.end());
    cout << "  " << "\"" << i.first << "\" : [";
    for (int j = 0; j < i.second.size(); j++) {
      if (j == 0) cout << i.second.at(j);
      else cout << ", " << i.second.at(j);
    }
    if (i.first == "한성") {
      cout << "]\n";
    }
    else {
      cout << "],\n";
    }
  }
  cout << "}";
}