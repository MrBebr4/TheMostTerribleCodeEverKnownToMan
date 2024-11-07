#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef enum {
    STATE_START,
    STATE_IN_NUMBER,
    STATE_INVALID
} State;

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

ssize_t getline(char **lineptr, size_t *n, FILE *stream) {
    if (lineptr == NULL || n == NULL || stream == NULL) {
        return -1;
    }

    size_t pos = 0;
    int c;

    if (*lineptr == NULL) {
        *n = 128;
        *lineptr = (char *)malloc(*n);
        if (*lineptr == NULL) {
            return -1;
        }
    }

    while ((c = fgetc(stream)) != EOF) {
        if (pos + 1 >= *n) {
            size_t new_size = *n * 2;
            char *new_ptr = (char *)realloc(*lineptr, new_size);
            if (new_ptr == NULL) {
                return -1;
            }
            *lineptr = new_ptr;
            *n = new_size;
        }
        (*lineptr)[pos++] = c;
        if (c == '\n') {
            break;
        }
    }

    if (pos == 0 && c == EOF) {
        return -1;
    }

    (*lineptr)[pos] = '\0';
    return pos;
}

void search_lexicographically_sorted_11_based_numbers(const char *input_filename, const char *output_filename) {
    FILE *input_file = fopen(input_filename, "r");
    if (input_file == NULL) {
        perror("Error opening input file");
        return;
    }

    FILE *output_file = fopen(output_filename, "w");
    if (output_file == NULL) {
        perror("Error opening output file");
        fclose(input_file);
        return;
    }

    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    while ((read = getline(&line, &len, input_file)) != -1) {
        State state = STATE_START;
        int start = 0;

        for (int i = 0; line[i] != '\0'; i++) {
            switch (state) {
                case STATE_START:
                    if (isdigit(line[i]) || line[i] == 'A') {
                        state = STATE_IN_NUMBER;
                        start = i;
                    }
                    break;
                case STATE_IN_NUMBER:
                    if (!(isdigit(line[i]) || line[i] == 'A')) {
                        char number[i - start + 1];
                        strncpy(number, &line[start], i - start);
                        number[i - start] = '\0';

                        if (is_11_based_number(number) && is_lexicographically_sorted(number)) {
                            fprintf(output_file, "Found lexicographically sorted 11-based number: %s\n", number);
                        }
                        state = STATE_START;
                    }
                    break;
                case STATE_INVALID:
                    state = STATE_START;
                    break;
            }
        }

        if (state == STATE_IN_NUMBER) {
            char number[strlen(line) - start + 1];
            strncpy(number, &line[start], strlen(line) - start);
            number[strlen(line) - start] = '\0';

            if (is_11_based_number(number) && is_lexicographically_sorted(number)) {
                fprintf(output_file, "Found lexicographically sorted 11-based number: %s\n", number);
            }
        }
    }

    free(line);
    fclose(input_file);
    fclose(output_file);
}

int main() {
    search_lexicographically_sorted_11_based_numbers("random_text.txt", "output.txt");
    return 0;
}