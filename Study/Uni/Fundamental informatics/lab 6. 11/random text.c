#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void generate_random_numbers(const char *file_name, size_t size_in_mb) {
    size_t size_in_bytes = size_in_mb * 1024 * 1024;
    FILE *file = fopen(file_name, "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return;
    }

    srand(time(NULL));
    size_t bytes_written = 0;
    while (bytes_written < size_in_bytes) {
        int num_digits = rand() % 9 + 1; // Random number of digits between 1 and 9
        for (int i = 0; i < num_digits; i++) {
            int digit = rand() % 11; // Random digit between 0 and 10
            if (digit == 10) {
                bytes_written += fprintf(file, "A");
            } else {
                bytes_written += fprintf(file, "%d", digit);
            }
        }
        bytes_written += fprintf(file, "\n"); // Add a newline after each number
    }

    fclose(file);
}

int main() {
    generate_random_numbers("random_numbers.txt", 10);
    return 0;
}