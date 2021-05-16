#include <stdarg.h>
#include <stdio.h>

// η συνάρτηση δέχεται ως πρώτο όρισμα το πλήθος των τιμών και στη συνέχεια τις ακέραιες τιμές και επιστρέφει το άθροισμά τους
int sum_all(int n, ...) {
  va_list args; // αρχικοποίηση του δείκτη των ορισμάτων
  va_start(args, n); // τοποθέτηση του δείκτη στο πρώτο (μη variadic) όρισμα.

  int sum = 0;
  for (int i = 0; i < n; i++) {
    int x = va_arg(args, int); // πρόσβαση στο επόμενο variadic όρισμα
    sum += x;
  }

  va_end(args); // τερματισμός διάσχισης των variadic ορισμάτων
  return sum;
}

int main() {
  printf("%d\n", sum_all(2, 10, 20));
  printf("%d\n", sum_all(3, 10, 20, 30));
  printf("%d\n", sum_all(4, 10, 20, 30, 40));
}

/*
30
60
100
*/