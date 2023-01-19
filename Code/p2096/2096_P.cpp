#include <iostream>
using namespace std;

int N, prevMinimum[3], curMinimum[3], prevMaximum[3], curMaximum[3], arr[3], minimum, maximum;

int main(){
    scanf("%d", &N);
    for (int i = 0; i < N; i++){
        for (int j = 0; j < 3; j++) {
            scanf("%d", &arr[j]);
            minimum = 2147483647, maximum = 0;
            for (int k = -1; k < 2; k++){
                if (j + k < 0 || j + k > 2) continue;
                minimum = prevMinimum[j + k] < minimum ? prevMinimum[j + k] : minimum;
                maximum = prevMaximum[j + k] > maximum ? prevMaximum[j + k] : maximum;
            }
            curMinimum[j] = minimum + arr[j];
            curMaximum[j] = maximum + arr[j];
        }

        for (int i = 0; i < 3; i++) {
            prevMinimum[i] = curMinimum[i];
            prevMaximum[i] = curMaximum[i];
        }
    }

    minimum = curMinimum[0], maximum = curMaximum[0];    
    for (int i = 0; i < 3; i++){
        minimum = minimum < curMinimum[i] ? minimum : curMinimum[i];
        maximum = maximum > curMaximum[i] ? maximum : curMaximum[i];
    }

    printf("%d %d", maximum, minimum);


}
