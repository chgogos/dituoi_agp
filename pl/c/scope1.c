#include <stdio.h>

int main() {
  int x = 1;
  {
    int x = 2;
    int y = 3;
    printf("x=%d at line %d\n", x, __LINE__);
    printf("y=%d at line %d\n", y, __LINE__);
  }
  printf("x=%d at line %d\n", x, __LINE__);
}


/*
x=2 at line 8
y=3 at line 9
x=1 at line 11
*/