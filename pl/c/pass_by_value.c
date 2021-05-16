#include <stdio.h>

// x μεταβίβαση κατά τιμή
// y μεταβίβαση κατά αναφορά
// z μεταβίβαση κατά αναφορά (μονόδρομη)
void fun1(int x, int *y, const int *z) {
  x++;
  (*y)++;
  //   (*z)++; // error: increment of read-only location '*z'
  printf("fun1: x=%d, y=%d, z=%d\n", x, *y, *z);
}

int main() {
  int a = 1, b = 1, c = 1;
  fun1(a, &b, &c);
  printf("main: a=%d, b=%d, c=%d\n", a, b, c);
}

/*
fun1: x=2, y=2, z=1
main: a=1, b=2, c=1
*/