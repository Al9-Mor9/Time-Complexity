#include <iostream>
#include <deque>
using namespace std;

deque<pair<int, int>> deq;

int main(){
    int N, L, A;
    scanf("%d%d", &N, &L);
    for (int i = 0; i< N; i++){
        scanf("%d", &A);
        if (!deq.empty() && deq.front().second < i - L + 1) deq.pop_front();
        while (!deq.empty() && deq.back().first >= A) deq.pop_back();
        deq.emplace_back(A, i);
        printf("%d ", deq.front().first);
    }    
}
