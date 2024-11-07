#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int is_lexicographically_sorted(const char *str) {
    for (int i = 1; str[i] != '\0'; i++) {
        if (str[i] < str[i - 1]) {
            return 0;
        }
    }
    return 1;
}

int is_11_based_number(const char *str) {
    for (int i = 0; str[i] != '\0'; i++) {
        if (!(isdigit(str[i]) || str[i] == 'A')) {
            return 0;
        }
    }
    return 1;
}

void search_lexicographically_sorted_11_based_numbers(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening file");
        return;
    }

    char line[1024];
    while (fgets(line, sizeof(line), file)) {
        for (int i = 0; line[i] != '\0'; i++) {
            if (isdigit(line[i]) || line[i] == 'A') {
                int j = i;
                while (line[j] != '\0' && (isdigit(line[j]) || line[j] == 'A')) {
                    j++;
                }
                char number[j - i + 1];
                strncpy(number, &line[i], j - i);
                number[j - i] = '\0';

                if (is_11_based_number(number) && is_lexicographically_sorted(number)) {
                    printf("Found lexicographically sorted 11-based number: %s\n", number);
                }
                i = j - 1;
            }
        }
    }

    fclose(file);
}

int main() {
    search_lexicographically_sorted_11_based_numbers("random_text.txt");
    return 0;
}