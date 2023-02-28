#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define MAXN 500000

vector<pair<int, int>> tmp; 
vector<int> ability;
int tree[MAXN * 4];

void insert(int start, int end, int root, int idx, int val){
	if (idx < start || end < idx) return;
	tree[root] +=  val;
	if (start == end) return;
	int mid = (start + end) / 2;
	insert(start, 	mid, root * 2, 		idx, val);
	insert(mid + 1, end, root * 2 + 1, 	idx, val);
}

int search(int start, int end, int root, int left, int right){
	if (left > end || right < start) return 0;
	if (left <= start && right >= end) return tree[root];
	int mid = (start + end) / 2;
	return search(start, mid, root * 2, left, right) + search(mid + 1, end, root * 2 + 1, left, right);
}

int main(){
	int N,n ;
	scanf("%d", &N);

	for (int i = 0; i < N; i++){
		scanf("%d", &n);
		tmp.push_back({n, i});		
	}

	sort(tmp.begin(), tmp.end());
	ability.resize(tmp.size());

	for (int i = 0; i < N; i++) {
		ability[tmp[i].second] = i;
	}

	for (int i = 0; i < N; i++){
		//printf("abil[%d]: %d\n", i, ability[i]);
		insert(0, N - 1, 1, ability[i], 1);
		int ans = search(0, N-1, 1, ability[i], N - 1);
		printf("%d\n", ans);
	}


}
