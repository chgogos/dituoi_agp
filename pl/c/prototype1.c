#include <stdio.h>

// prototype της συνάρτησης fun
int fun1(int a, int b);

int main() {
  int x = 1, y = 2, z;
  z = fun1(x, y);
  printf("z=%d\n", z);
}

int fun1(int a, int b) { return a + b; }
