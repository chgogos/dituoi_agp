// Η C δεν υποστηρίζει υπερφόρτωση συναρτήσεων

#include <stdio.h>

int fun(int x) {
  // dummy
  return 0;
}

int fun(char x) { // error: conflicting types for 'fun'
  // dummy
  return 0;
}

int main() {}