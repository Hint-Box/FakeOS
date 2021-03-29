#include <stdio.h>

int main(void) {
  FILE *csv_file;
  char char_from_file, file_path[150], file_content[500];

  printf("Enter the file path: ");
  scanf("%s", &file_path);

  csv_file = fopen(file_path, "r");

  for (unsigned short i = 0; i < 500; i++) {
    char_from_file = fgetc(csv_file);
    if (char_from_file != EOF) {
      file_content[i] = char_from_file;
    }
    else {
      break;
    }
  }

  for (unsigned short i = 0; i < 500; i++) {
    printf("%c", file_content[i]);
  }

  return 0;
}
