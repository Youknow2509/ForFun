#include<iostream>

using namespace std;


int main(){
	int n;
	cin >> n;
	int *arr = new int[n];
	for(int i=0; i < n; i++){
		cin >> arr[i];
	}
	int s = 0;
	for(int i=0; i < n; i++){
		if(arr[i] % 3 == 0 && arr[i] % 5 != 0  )
		cout << arr[i] <<" ";
	}
	
	delete[]arr; 
	// Khi dùng mảng cáp phát động, mở mảng cấp phát động ta cần xóa không sẽ bị tràn data, và nặng bộ nhớ, nó chỉ xóa đi khi tắt máy. DỄ GÂY RA LỖI
	return 0;

}





