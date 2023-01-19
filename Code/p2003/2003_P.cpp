#include <iostream>
using namespace std;

int main(){
    int A[10000];
    int N, M, idx1 = 0, idx2 = 0, sum = 0, ans = 0;

    scanf("%d%d", &N, &M);
    for (int i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }
    sum = A[0];
    while (idx2 < N){
        if (sum > M){
            sum -= A[idx1++];
        }
        else {
            ans += (sum == M);
            if (++idx2 < N) {
                sum += A[idx2];
            }
        }
    }    
    printf("%d", ans);
}
