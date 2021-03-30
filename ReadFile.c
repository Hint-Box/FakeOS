#include <stdio.h>
#include <stdlib.h>
#define CHAR_SIZE sizeof (char)

/* A little experiment to try to read CSV files using C instead of Python.
 * The code here will later be translated to Cython.
 */

int main(void) {

  // Variables declaration
  FILE *csv_file;
  char char_from_file, *tmp_str = malloc(4096 * CHAR_SIZE);
  unsigned int len_tmp_str, num_of_chars = 0;

  // Get the file path from the user
  printf("Enter the file path: ");
  scanf("%s", tmp_str);

  // Open the file and check for errors
  printf("Opening %s...\n", tmp_str);
  csv_file = fopen(tmp_str, "r");

  if (csv_file == NULL) {
    printf("ERROR: Could not open the file.\n");
    exit(0);
  }

  // Get the number of characters in the file
  while (fgetc(csv_file) != EOF) {
    num_of_chars++;
  }
  printf("The file has %d characters.\n", num_of_chars);

  // Allocate memory for the array that is going to contain the file's content
  len_tmp_str = num_of_chars * CHAR_SIZE;
  tmp_str = realloc(tmp_str, len_tmp_str);
  if (tmp_str == NULL) {
    printf("ERROR: Could not allocate enough memory for the array.");
    exit(0);
  }

  // Loop through the file again to store each character in the previous array
  fseek(csv_file, 0, SEEK_SET);
  for (unsigned int i = 0; i < len_tmp_str; i++) {
    char_from_file = fgetc(csv_file);

    if (char_from_file != EOF) {
      tmp_str[i] = char_from_file;
      printf("%c", char_from_file);
    }
    else {
      break;
    }
  }

  // End of the program
  printf("\nFinalized.\n");
  return 0;
}
