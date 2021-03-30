#include <stdio.h>
#include <stdlib.h>

/* A little experiment to try to read CSV files using C instead of Python.
 * The code here will later be translated to Cython.
 */

int main(void)
{
  FILE *csv_file;
  char char_from_file, *mem_for_str = malloc(4096 * sizeof (char));
  unsigned int len_mem_for_str, num_of_chars = 0;

  printf("Enter the file path: ");
  scanf("%s", mem_for_str);

  printf("Opening %s...\n", mem_for_str);
  csv_file = fopen(mem_for_str, "r");

  if (csv_file == NULL)
  {
    printf("ERROR: Could not open the file.\n");
    exit(0);
  }

  while (fgetc(csv_file) != EOF) num_of_chars++;
  fseek(csv_file, 0, SEEK_SET);
  printf("The file has %d characters.\n", num_of_chars);

  len_mem_for_str = num_of_chars * sizeof(char)
  mem_for_str = realloc(mem_for_str, len_mem_for_str);

  if (mem_for_str == NULL) {
    printf("ERROR: Could not allocate enough memory for pointer of type char.");
    exit(0);
  }

  for (unsigned int i = 0; i < len_mem_for_str; i++)
  {
    char_from_file = fgetc(csv_file);
    if (char_from_file != EOF)
    {
      mem_for_str[i] = char_from_file;
      printf("%c", char_from_file);
    }
    else break;
  }

  printf("\nFinalized.\n");

  return 0;
}
