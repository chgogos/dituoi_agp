#include <stdio.h>

int g = 100;

int fun1() {
  extern int e;
  printf("%d e=%d\n", __LINE__, e);
  printf("%d g=%d\n", __LINE__, g);
}

int e = 3;

int main() {
  int a = 1;
  printf("%d a=%d\n", __LINE__, a);
  printf("%d e=%d\n", __LINE__, e);
  printf("%d g=%d\n", __LINE__, g);
  fun1();
}

/*
15 a=1
16 e=3
17 g=100
7 e=3
8 g=100
*/