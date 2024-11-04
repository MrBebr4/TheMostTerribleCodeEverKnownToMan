#include <stdio.h>
#include <stdbool.h>

// Function to check if a number is lexicographically sorted
bool is_lexicographically_sorted(const char *num_str) {
    for (int i = 1; num_str[i] != '\0'; i++) {
        if (num_str[i] < num_str[i - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    FILE *file = fopen("random_numbers.txt", "r");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    char num_str[10];
    printf("11-based numbers with lexicographically sorted digits:\n");
    while (fscanf(file, "%9s", num_str) != EOF) {
        if (is_lexicographically_sorted(num_str)) {
            printf("%s\n", num_str);
        }
    }

    fclose(file);

    // Wait for user input before closing
    printf("Press any key to exit...\n");
    getchar();

    return 0;
}