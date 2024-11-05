#include <stdio.h>
#include <stdbool.h>

// Функция для проверки, отсортированы ли цифры числа лексикографически
bool is_lexicographically_sorted(const char *num_str) {
    // Проходит по каждому символу строки, начиная со второго
    for (int i = 1; num_str[i] != '\0'; i++) {
        // Сравнивает текущий символ с предыдущим
        if (num_str[i] < num_str[i - 1]) {
            // Если текущий символ меньше предыдущего, возвращает false
            return false;
        }
    }
    // Если все символы проверены и ни одно сравнение не нарушено, возвращает true
    return true;
}

int main() {
    // Открывает файл random_numbers.txt для чтения
    FILE *file = fopen("random_numbers.txt", "r");
    if (file == NULL) {
        // Если файл не удается открыть, выводит сообщение об ошибке и завершает программу с кодом возврата 1
        printf("Error opening file.\n");
        return 1;
    }

    char num_str[10];
    // Выводит заголовок для чисел, отсортированных лексикографически
    printf("11-based numbers with lexicographically sorted digits:\n");
    // Читает числа из файла построчно
    while (fscanf(file, "%9s", num_str) != EOF) {
        // Для каждого числа проверяет, отсортированы ли его цифры лексикографически
        if (is_lexicographically_sorted(num_str)) {
            // Если число отсортировано, выводит его на экран
            printf("%s\n", num_str);
        }
    }

    // Закрывает файл
    fclose(file);

    // Ожидание нажатия клавиши перед завершением
    printf("Press any key to exit...\n");
    getchar();

    return 0;
}