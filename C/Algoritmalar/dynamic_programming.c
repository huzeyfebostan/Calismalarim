#include <stdio.h>
#include <string.h>

int max (int a, int b)
{
  if (a >= b)
    return (a);
  else if (b >= a)
    return (b);
  return (0);
}

void str_comparison(char *str1, char *str2, int len1, int len2)
{
  int max_num = 0, row = len1, col = len2;
  int grid[row][col];
  for (int i = 0; i < row; i++)
  {
    for (int j = 0; j < col; j++)
    {
      if (str1[i] == str2[j])
      {
        if (i == 0 || j == 0)
          grid[i][j] = 1;
        else
          grid[i][j] = grid[i-1][j-1] + 1;
      }
      else
        grid[i][j] = 0;
      //printf("%d",grid[i][j]);
      if(max(grid[i][j], grid[i][j]) > max_num)
        max_num = max(grid[i][j], grid[i][j]);
    }
    //printf("\n");
  }
  printf("%d\n",max_num);
}

int main(int argc, char **argv) 
{
  int i, str1_len, str2_len;
  char  *str1, *str2;

  str1_len = strlen(argv[1]);
  str2_len = strlen(argv[2]);
  str1 = argv[1];
  str2 = argv[2];
  str_comparison(str1, str2, str1_len, str2_len);
}