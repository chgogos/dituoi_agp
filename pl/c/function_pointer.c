#include <stdio.h>

double foo(int x) {
  printf("double foo(int)\n");
  return 3.14;
}

double bar(int x) {
  printf("double bar(int)\n");
  return 2.718;
}

int main() {
  double (*f)(int) = &foo;
  double r = f(1);
  printf("%f\n", r);

  f = &bar;
  r = f(2);
  printf("%f\n", r);
}

/*
double foo(int)
3.140000
double bar(int)
2.718000
*/