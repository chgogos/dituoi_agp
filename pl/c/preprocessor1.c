// gcc -E preprocessor1.c
#include <stdio.h>

#define max(A, B) ((A) > (B) ? (A) : (B))

int main() {
  double x, y = 2.7, z = 13.1;
  x = max(2 * y, z / 1.7);
  printf("%.f\n", x);
}

/*
# 1 "preprocessor1.c"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "preprocessor1.c"




int main(){
    double x, y=2.7, z=13.1;
    x = ((2*y)>(z/1.7) ? (2*y):(z/1.7));
}
*/
