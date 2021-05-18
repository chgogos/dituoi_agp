#include <stdio.h>

#define mat_ptr(r, c) (*(mat_ptr + ((r) * N) + c)))

void fun(int *mat_ptr, int M, int N) {
  for (int i = 0; i < M; i++) {
    for (int j = 0; j < N; j++) {
      printf("%3d", mat_ptr(i,j);
    }
    printf("\n");
  }
}

int main() {
  int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
  fun(a, 4, 3);
  printf("\n");
  fun(a, 3, 4);
}

/*
  1  2  3
  4  5  6
  7  8  9
 10 11 12

  1  2  3  4
  5  6  7  8
  9 10 11 12
*/