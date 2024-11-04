#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <stdbool.h>

int min(int a, int b) {
    if (a <= b) {
        return a;
    } else {
        return b;
    }
}

int max(int a, int b) {
    if (a >= b) {
        return a;
    } else {
        return b;
    }
}

int mod(int a, int b) {
    if (b == 0) {
        return 0;
    }
    int result = a % b;
    if (result < 0) {
        result += (b > 0) ? b : -b;
    }

    return result;
}
int sign(int a) {
    if (a > 0) {
        return 1;
    } else if (a == 0) {
        return 0;
    } else {
        return -1;
    }
}

bool isPointInRing(int x, int y) {
    int centerX = 10;
    int centerY = 10;
    int innerRadius = 5;
    int outerRadius = 10;

    // Вычисляем расстояние от точки до центра
    int distance = sqrt((x - centerX) * (x - centerX) + (y - centerY) * (y - centerY));
    // Проверяем, попадает ли точка в кольцо
    return (distance >= innerRadius && distance <= outerRadius);
}


int main(void) {
    int i[51]; i[0]=18;
    int j[51]; j[0]=-9;
    int l[51]; l[0]=5;
    bool flag = false;
    for (int k = 0;k<50;k++){
        i[k+1] = mod(i[k] * max(j[k], l[k]), 30) + mod(j[k] * min(i[k], l[k]), 20) + k;
        j[k+1] = min(i[k], max(j[k], min(l[k], max(i[k]- l[k], j[k] - l[k]))));
        l[k+1] = sign(k-10)*abs(i[k]-j[k]+l[k]-k);
        if (isPointInRing(i[k], j[k])) {flag=true; printf("%s, %d, %d, %d", "Hit", i[k], j[k] , l[k]); break;}
    }
    if (flag==false) printf("%s, %d, %d, %d", "Miss", i[50], j[50] , l[50]);
    getchar();
}