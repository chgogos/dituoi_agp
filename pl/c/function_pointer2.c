#include <stdio.h>

int fun(int a, int b) { return a + b; }

int main() {
  int (*ptr)(int, int);
  ptr = &fun; // ή ptr = fun;

  int result;
  result = (*ptr)(1, 2); // ή ptr(1,2); ή fun(1,2);

  printf("%d\n", result);
}