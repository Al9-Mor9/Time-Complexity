#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int height[1000000], high, low, middle, ans;
long long sum;

int main(){
    scanf("%d%d", &N, &M);
    for (int i = 0; i < N; i++) {
        scanf("%d", &height[i]);
        high = height[i] < high ? high : height[i];
    }
    sort(height, height + N);

    while (low <= high){ 
        middle = (low + high) / 2;
        sum = 0;
        for (int i = upper_bound(height, height + N, middle) - height; i < N; i++){
            sum += (middle - height[i] >= 0 ? 0 : height[i] - middle);
        }
        if (sum < M) high = middle - 1;
        else {
            low = middle + 1;
            ans = middle;
        } 
    }

    printf("%d", ans);
}
