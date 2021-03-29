#include <stdio.h>
#include <stdlib.h>

/* A little experiment to try to read CSV files using C instead of Python.
 * The code here will later be translated to Cython.
 */

int main(void) {
  FILE *csv_file;
  char char_from_file, *file_path = malloc(500 * sizeof(char));
  unsigned int file_size;

  printf("Enter the file path: ");
  scanf("%s", file_path);

  printf("Opening %s...\n", file_path);

  csv_file = fopen(file_path, "r");
  if (csv_file == NULL) {
    printf("ERROR: Could not open the specified file.");
    exit(0);
  }

  free(file_path);  // Free the memory of file_path

  // Get the size of the file in characters to allocate memory for the array
  file_size = 0;
  while (fgetc(csv_file) != EOF) {
    file_size++;
  }

  printf("The file has %d characters\n", file_size);

  // Store the contents of the file and print each character
  char file_content[file_size];
  fseek(csv_file, 0, SEEK_SET);

  for (unsigned short i = 0; i < file_size; i++) {
    char_from_file = fgetc(csv_file);

    if (char_from_file != EOF) {
      file_content[i] = char_from_file;
      printf("%c", file_content[i]);
    }
    else {
      break;
    }
  }
  fclose(csv_file);

  return 0;
}
