#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Constants
#define MAX_STEPS 50
#define RADIUS 10
#define CENTER_X 0
#define CENTER_Y 0

// Function to update coordinates and dynamic parameter
void obnovit_koordinaty(int i, int j, int l, int k) {
    int sleduyushchiy_i = (i + (int)fmax(j, l)) % 30 + (j + (int)fmin(i, l)) % 20 + k;
    int sleduyushchiy_j = (int)fmin(i, (int)fmax(j, (int)fmin(i, (int)fmax(i - l, j - l))));
    int sleduyushchiy_l = (k - 10 >= 0 ? 1 : -1) * abs(i - j + l - k);

    *i = sleduyushchiy_i;
    *j = sleduyushchiy_j;
    *l = sleduyushchiy_l;
}

// Function to check if the point is within the target area
int vnutri_celevoy_oblasti(int i, int j) {
    int dist = (i - CENTER_X) * (i - CENTER_X) + (j - CENTER_Y) * (j - CENTER_Y);
    return dist <= RADIUS * RADIUS;
}

// Function to print the result
void pechat_rezultata(int shagi, int i, int j, int l, int uspeh) {
    if (uspeh) {
        printf("Tochka dostigla celevoy oblasti za %d shagov.\n", shagi);
    } else {
        printf("Tochka ne dostigla celevoy oblasti za %d shagov.\n", shagi);
    }
    printf("Konechnoe vremya: %d\n", shagi);
    printf("Konechnye koordinaty: (%d, %d)\n", i, j);
    printf("Znachenie dinamicheskogo parametra: %d\n", l);
}

int main() {
    int i = 18;
    int j = -9;
    int l = 5;
    int k;
    scanf("%i", &k);

    for (int shag = 1; shag < MAX_STEPS; shag++) {
        obnovit_koordinaty(&i, &j, &l, k);

        if (vnutri_celevoy_oblasti(i, j)) {
            pechat_rezultata(k + 1, i, j, l, 1);
            return 0;
        }
    }

    pechat_rezultata(MAX_STEPS, i, j, l, 0);
    return 0;
}