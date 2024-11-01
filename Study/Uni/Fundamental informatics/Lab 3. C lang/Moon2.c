
#include <stdio.h>
#include <math.h>

// Константы
#define MAX_STEPS 50
#define RADIUS 10
#define CENTER1_X -10
#define CENTER1_Y -10
#define CENTER2_X -20
#define CENTER2_Y -20
#define START_I 13
#define START_J -9
#define START_L 10

void update_coordinates(int *i, int *j, int *l, int k) {
    int next_i = ((*i + *j) % 30) / (1 % 5 + 1) + ((*i + *l) % 30) / (abs(*j) % 5 + 1);
    int next_j = fmax(k * (k + 1) * *j % 25 - *j - *l / 10, 0);
    int next_l = *j - *l / 10 + fmin((*i + 1) % 20, *j % 20) - 10;

    *i = next_i;
    *j = next_j;
    *l = next_l;
}

int is_within_target_area(int i, int j) {
    int dist1 = (i - CENTER1_X) * (i - CENTER1_X) + (j - CENTER1_Y) * (j - CENTER1_Y);
    int dist2 = (i - CENTER2_X) * (i - CENTER2_X) + (j - CENTER2_Y) * (j - CENTER2_Y);

    return (dist1 <= RADIUS * RADIUS && dist2 <= RADIUS * RADIUS);
}

void print_result(int steps, int i, int j, int l, int success) {
    if (success) {
        printf("Point reached the target area in %d steps.\n", steps);
    } else {
        printf("Point did not reach the target area in %d steps.\n", steps);
    }
    printf("End time: %d\n", steps);
    printf("Final coordinates: (%d, %d)\n", i, j);
    printf("Dynamic parameter value: %d\n", l);
}

int main() {
    int i = START_I;
    int j = START_J;
    int l = START_L;
    int k;

    printf("Enter the value for k: ");
    scanf("%d", &k);

    for (int step = 0; step < MAX_STEPS; step++) {
        update_coordinates(&i, &j, &l, k);

        if (is_within_target_area(i, j)) {
            print_result(step + 1, i, j, l, 1);
            getchar();
            return 0;
        }
    }

    print_result(MAX_STEPS, i, j, l, 0);
    getchar();
    return 0;
}