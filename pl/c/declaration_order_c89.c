#include <stdio.h>

int main() {
  int sum = 0;

  for (int i = 0; i < 10; i++) {
    sum += i;
  }
}

/*
$ gcc .\declaration_order_c89.c -std=c89

error: 'for' loop initial declarations are only allowed in C99 or C11 mode
*/