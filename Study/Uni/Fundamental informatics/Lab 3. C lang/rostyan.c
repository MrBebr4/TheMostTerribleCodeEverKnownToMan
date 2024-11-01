#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Constants
#define MAX_STEPS 50
#define RADIUS 10
#define CENTER_X 0
#define CENTER_Y 0


// Function to update coordinates and dynamic parameter
void update_coordinates(int i, int j, int l, int k) {
    int next_i = (i + (int)fmax(j,l)) % 30 + (j + (int)fmin(i, l)) % 20 + k;
    int next_j = (int)fmin(i, (int)fmax(j, (int)fmin(i, (int)fmax(i -l, j -l))));
    int next_l = (k - 10 >= 0 ? 1 : -1) * abs(i -j + *l - k);

    *i = next_i;
    *j = next_j;
    *l = next_l;
}

// Function to check if the point is within the target area
int is_within_target_area(int i, int j) {
    int dist = (i - CENTER_X) (i - CENTER_X) + (j - CENTER_Y) * (j - CENTER_Y);
    return dist <= RADIUS * RADIUS;
}

// Function to print the result
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
    int i = 18;
    int j = -9;
    int l = 5;
    int k;
    scanf("%i", &k);


    for (int step = 1; step < MAX_STEPS; step++) {
        update_coordinates(&i, &j, &l, k);

        if (is_within_target_area(i, j)) {
            print_result(k + 1, i, j, l, 1);
            return 0;
        }
    }

    print_result(MAX_STEPS, i, j, l, 0);
    return 0;
}