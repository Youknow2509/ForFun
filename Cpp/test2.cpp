#include<iostream>

using namespace std;

int main() {
    int tong_cac_hang[10000000];
    int tong = 0;
    int n , m;
	cout << "Nhap so hang va so cot " ;
    cin >> n >> m;
    int s[n][m];
    // nhap mang 
    for( int i = 0; i <n ;i++){
		for(int j = 0; j < m ;j ++){
            cin >> s[i][j];

		    }
        }
    // cho tong vao mang moi
     for( int i = 0; i <n ;i++){
		for(int j = 0; j < m ;j ++){
            tong = tong + s[i][j];
            } 
            // tinh tong 
        for(int t =0 ; t < n; t ++){
            tong_cac_hang[t] = tong;
            tong = 0;}
    }
    for(int t =0 ; t < n; t ++){
        cout<<" Tong cua hang"<< t+1 <<"la" <<tong_cac_hang[t]; 
    }
    return 0;
}