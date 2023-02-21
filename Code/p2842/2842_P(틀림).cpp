#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int N, homeCnt;
char town[50][50];
int height[50][50];
bool visited[50][50];
pair<int, int> startPos;
int highest = 0, lowest = 1000000;

int dir[8][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1},{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

int diff(pair<int, int> &p){
    if (lowest <= height[p.first][p.second] && height[p.first][p.second] <= highest) return 0;
    if (height[p.first][p.second] < lowest) return lowest - height[p.first][p.second]; 
    if (height[p.first][p.second] > highest) return height[p.first][p.second] - highest;
}

bool isInBound(pair<int, int> &p){
    if (p.first < 0) return false;
    if (p.first >= N) return false;
    if (p.second < 0) return false;
    if (p.second >= N) return false;
    return true;
}

struct compare{
    bool operator()(pair<int, int> &p1, pair<int, int> &p2) {
        return diff(p1) > diff(p2);
    }
};

priority_queue<pair<int, int>, vector<pair<int, int>>, compare> pq;

void bfs(){
    while (!pq.empty() && homeCnt){
        pair<int, int> top = pq.top();
        //rintf("(%d, %d) : %d, diff : %d\n", top.first, top.second, height[top.first][top.second], diff(top));
        if (town[top.first][top.second] == 'K') homeCnt--;
        if (height[top.first][top.second] < lowest) lowest = height[top.first][top.second];
        if (height[top.first][top.second] > highest) highest = height[top.first][top.second];
        pq.pop();
        for (int i = 0; i < 8; i++){
            pair<int, int> next = {top.first + dir[i][0], top.second + dir[i][1]};
            if (!isInBound(next)) continue;
            if (visited[next.first][next.second]) continue;
            visited[next.first][next.second] = true;
            pq.push(next);
        }
    }
}

int main(){
    scanf("%d", &N);
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            scanf("\n%c", &town[i][j]);
            if (town[i][j] == 'P') {
                startPos = {i, j};
            }
            else if (town[i][j] == 'K') homeCnt++;
        }
    }
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            scanf("%d", &height[i][j]);
            if (town[i][j] == '.') continue;
            if (height[i][j] < lowest) {
                lowest = height[i][j];
            }
            if (height[i][j] > highest){
                highest = height[i][j];
            }
        }
    }
    pq.push(startPos);
    visited[startPos.first][startPos.second] = true;
    bfs();
    //printf("ans? %d, high: %d, low: %d", highest - lowest, highest, lowest);
    printf("%d", highest - lowest);
}
