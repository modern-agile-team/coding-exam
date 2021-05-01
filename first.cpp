#include <iostream>
#include <string>
#include <cstring>
#define _CRT_SECURE_NO_WARNINGS

using namespace std;
/*
class WOAHAN {
private:
	string zumsu;
	int count = 0;
	int avg;
	
public:
	WOAHAN() { cout << "무야호" << endl; }
	~WOAHAN() {}
	int getAvg(string zumsu) {
		
	}
	void setZumsu(string zumsu);

};
void WOAHAN::setZumsu(string zumsu){
	this->zumsu = zumsu;
};
*/
int main(void)
{
	char *str[200];
	int count = 0;
	char stu[200];
	char* num;
	int avg;

	cout << "0과 100 사이의 점수를 콤마와 띄어쓰기를 이용하여 입력하세요" << endl;
	cin >> stu[200];
	for (num = strtok(stu, ", "); num; num = strtok(NULL, ", "))
		str[count++] = num;
	while(count > 0)
		str[--count]
	/*
	string zumsu;
	string str_arr[100];
	
	string *stu = new string[];
	if (!stu) { cout << "동적할당 실패" << endl; exit(1); }
	cin >> *zumsu;
	stu = *zumsu;
	char *chul = strtok_s(stu[]," ");

	while (chul != nullptr) {
		str_arr[num++] = string(chul);
		chul = strtok(nullptr, " ");
	}
	*/
	
	
	/* ㅋㅋㅋㅋㅋ 죄송합니다... 사실 준비 못 했어요
	int num;
	
	string zumsu;
	

	

	cout << "애자일 학생의 과목 개수를 입력하세요" << endl;
	while (num < 1 && num > 100) {
		cin >> num;
		if (num < 1 && num > 100) {
			cout << "과목 개수를 다시 입력하세요" << endl;
			exit(1);
		}
	}
	WOAHAN *stu = new WOAHAN[num];
		
	if (!stu) { cout << "동적할당 실패" << endl; exit(1); }

	cout << "\n애자일 학생의 점수를 입력하세요" << endl;
	
	for (int k = 0; k < num; k++) {
		cin >> zumsu;
		stoi(zumsu);
		stu[k].setZumsu(zumsu);
	}
	
	cout << "평균은" << endl;
	cout << (stu[num].getZumsu() / num) << "입니다." << endl;

	delete[]stu;
	*/
	return 0;
}