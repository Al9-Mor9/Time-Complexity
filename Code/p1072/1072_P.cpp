#include <iostream>
using namespace std;

int main(){
    long long x, y, z;
    scanf("%lld%lld", &x, &y);
    z = 100 * y / x;
    if (z >= 99) printf("-1");
    else printf("%lld",  ((x * z) + x - (100 * y) - 1) / (99 - z) + 1);
}
