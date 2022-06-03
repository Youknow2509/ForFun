#include <iostream>

using namespace std;

int sum(int n) {
    if (n == 1) return 1;
    //   6 + 5 + 4 + 3 + 2 + 1

    if (n % 2 == 0) {
        return sum(n-1);
    } else {
      return n + sum(n-1);
    }
}

int main() {
    cout <<"Ham tinh tong so le tu 1 den n:";
    int n;
    cin >> n;
    cout << sum(n);
    return 0;
}