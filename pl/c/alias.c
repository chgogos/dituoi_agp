#include <stdio.h>

int main() {
  int x = 10;
  int *p = &x;

  *p = 20;

  printf("x = %d\n", x);
  printf("*p = %d\n", *p);
}

/*
x = 20
*p = 20
*/