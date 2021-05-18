#include <stdio.h>

void fun1(int matrix[4][3]) {
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 3; j++) {
      printf("%3d", matrix[i][j]);
    }
    printf("\n");
  }
}

void fun2(int matrix[][3]) {
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 3; j++) {
      printf("%3d", matrix[i][j]);
    }
    printf("\n");
  }
}

int main() {
  int mat[4][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {10, 11, 12}};
  fun1(mat);
  printf("\n");
  fun2(mat);
}

/*
  1  2  3
  4  5  6
  7  8  9
 10 11 12

  1  2  3
  4  5  6
  7  8  9
 10 11 12
*/