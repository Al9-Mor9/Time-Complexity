#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, A[4][4000];
long long aIdx, bIdx, nextAIdx, nextBIdx, ans;
vector<int> sumA, sumB;


int main(){
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        for (int j = 0; j < 4; j++){
            scanf("%d", &A[j][i]);
        }
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            sumA.push_back(A[0][i] + A[1][j]);
            sumB.push_back(A[2][i] + A[3][j]);
        }
    }

    sort(sumA.begin(), sumA.end());
    sort(sumB.begin(), sumB.end());

    while (true){
        if (aIdx == sumA.size()) break;
        bIdx = lower_bound(sumB.begin(), sumB.end(), -sumA[aIdx]) - sumB.begin();
        nextAIdx = upper_bound(sumA.begin(), sumA.end(), sumA[aIdx]) - sumA.begin();
        if (sumA[aIdx] + sumB[bIdx] == 0){
            nextBIdx = upper_bound(sumB.begin(), sumB.end(), sumB[bIdx]) - sumB.begin();
            ans += (nextAIdx - aIdx) * (nextBIdx - bIdx);
        }
        aIdx = nextAIdx;
    }    

    printf("%lld", ans);
}
