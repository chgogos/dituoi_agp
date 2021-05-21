#include <stdio.h>

void fun(int a, float b) { printf("%d %.2f\n", a, b); }
void foo(int a, float b) { printf("XXXXX %d %.2f\n", a, b); }

int main() {

  void (*fp)(int, float);

  fp = fun;
  fp(1, 3.14);
  fp = foo;
  fp(1, 3.14);
}