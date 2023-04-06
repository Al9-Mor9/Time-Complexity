#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int N;
char town[50][50];
vector<pair<int, int>> homes;
pair<int, int> office;
int height[50][50];
vector<int> heightVector;
int maxHeight = 0, minHeight;

int d[8][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

bool bfs(){
	queue<pair<int, int>> q;
	int cnt = 0;
	q.push(office);
	
	bool visited[50][50] = {false, };
	visited[office.first][office.second] = true;
	
	while (!q.empty()){
		pair<int, int> front = q.front();
		q.pop();
		for (int i = 0; i < 8; i++){
			int nx = front.first + d[i][0];
			int ny = front.second + d[i][1];
			if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
			if (visited[nx][ny]) continue;
			if (height[nx][ny] < minHeight || height[nx][ny] > maxHeight) continue;
			if (town[nx][ny] == 'K') cnt++;
			visited[nx][ny] = true;
			q.push({nx, ny});
		}
	}
	return cnt == homes.size();
}

int main(){
	scanf("%d", &N);
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			scanf("\n%c", &town[i][j]);
			if (town[i][j] == 'P'){
				office = {i, j};
			}
			else if (town[i][j] == 'K'){
				homes.push_back({i, j});
			}
		}
	}
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			scanf("%d", &height[i][j]);
			heightVector.push_back(height[i][j]);
		}
	}

	sort(heightVector.begin(), heightVector.end());

	maxHeight = height[office.first][office.second];
	minHeight = heightVector[0];
	
	int maxIdx = lower_bound(heightVector.begin(), heightVector.end(), maxHeight) - heightVector.begin();
	int officeIdx = maxIdx;
	int minIdx = 0;
	int ans = 2147483647;

	while (maxIdx <heightVector.size() && minIdx <= officeIdx){
		if (bfs()){
			ans = maxHeight - minHeight < ans ? maxHeight - minHeight : ans;
			minIdx = upper_bound(heightVector.begin(), heightVector.end(), minHeight) - heightVector.begin();
			minHeight = heightVector[minIdx];
		}
		else {
			maxIdx = upper_bound(heightVector.begin(), heightVector.end(), maxHeight) - heightVector.begin();
			maxHeight = heightVector[maxIdx];
		}
	}
	printf("%d", ans);
}
