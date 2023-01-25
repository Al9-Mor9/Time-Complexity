#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int T, n, m, A[1000], B[1000], sum;
    long long ans, aIdx, nextAIdx, bIdx, nextBIdx;
    vector<int> sumA, sumB;
    scanf("%d", &T);
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &A[i]);
    }

    for (int i = 0; i < n; i++){
        sum = 0;
        for (int j = i; j < n; j++){
            sumA.push_back(sum += A[j]);
        }
    }
    scanf("%d", &m);
    for (int i = 0; i < m; i++){
        scanf("%d", &B[i]);
    }
    for (int i = 0; i < m; i++){
        sum = 0;
        for (int j = i; j < m; j++){
            sumB.push_back(sum += B[j]);
        }
    }

    sort(sumA.begin(), sumA.end());
    sort(sumB.begin(), sumB.end());

    ans = 0;
    aIdx = bIdx = 0;
    nextAIdx = nextBIdx = 0;

    while(1){
        if (nextAIdx == sumA.size()) break;
        bIdx = lower_bound(sumB.begin(), sumB.end(), T - sumA[aIdx]) - sumB.begin();
        nextAIdx = upper_bound(sumA.begin(), sumA.end(), sumA[aIdx]) - sumA.begin();
        if (sumA[aIdx] + sumB[bIdx] == T) {
            nextBIdx = upper_bound(sumB.begin(), sumB.end(), sumB[bIdx]) - sumB.begin();
            ans += (nextAIdx - aIdx) * (nextBIdx - bIdx); 
            bIdx = nextBIdx;
        }
        aIdx= nextAIdx;
    }
    printf("%lld", ans);
}
