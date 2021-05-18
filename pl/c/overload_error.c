#include <stdio.h>

int fun(int x) {
  // dummy
  return 0;
}

float fun(int x) { // error: conflicting types for 'fun'
  // dummy
  return 0.0;
}

int main() {}