#include <iostream>
#include <cstring>
using namespace std;

int main() {
	/*cout << "암호를 입력하세요" << endl;
	char pwd[100];
	
	while (true) {
		cout << "암호: ";
		cin >> pwd;
		if (strcmp(pwd, "C++") == 0) {
			cout << "프로그램을 정상 종료합니다." << endl;
			break;
		}

		else {
			cout << "암호가 틀립니다." << endl;
		}
	}*/
	// 숙제: 아래와 같이 아래의 line 5~9같이 주소를 계속 입력받아 출력한다. 단, 사용자가 주소입력 없이 엔터만 치면
	// 프로그램을 종료한다.
	// 전처리기에서 '물리적으로' 헤더파일이 추가가 된다.
	cout << "주소를 입력하세요: ";
	char addr[100];
	cin.getline(addr, 100, '\n');
	// cin >> addr;
	cout << "주소는 " << addr << " 입니다." << endl;
	return 0;
}