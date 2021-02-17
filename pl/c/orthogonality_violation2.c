/*
Ένα μέλος μιας δομής μπορεί να είναι οποιουδήποτε τύπου δεδομένων εκτός από void
ή μια δομή του ίδιου τύπου. Ωστόσο, ένα μέλος μιας δομής μπορεί να είναι δείκτης
προς void ή δείκτης προς δομή του ίδιου τύπου.
*/

#include <stdio.h>

struct my_struct1 {
  int a;
  float b;
  char c;
  double d;
  int e[3];
};

// struct my_struct2{
//     struct my_struct2 a; // error: field 'a' has incomplete type
// };

// struct my_struct3{
//     void a; //  error: variable or field 'a' declared void
// };

struct my_struct3 {
  int a;                // 4
  float b;              // 4
  char c;               // 1
  double d;             // 8
  int e[3];             // 12
  struct my_struct3 *f; // 8
  void *g;              // 8
};

int main() {
  struct my_struct3 x, y;
  int z = 42;
  x.a = 1;
  x.b = 3.14;
  x.c = 'a';
  x.d = 2.718;
  x.e[0] = 1;
  x.e[1] = 2;
  x.e[2] = 3;
  x.f = &y;
  x.g = &z;

  printf("x.a=%d\n", x.a);
  printf("x.b=%f\n", x.b);
  printf("x.c=%c\n", x.c);
  printf("x.d=%f\n", x.d);
  printf("x.e=%d,%d,%d\n", x.e[0], x.e[1], x.e[2]);
  printf("x.f points to a struct of size %d bytes\n",
         sizeof(*x.f)); // padding occurs
  printf("x.g=%d\n", *((int *)x.g));
}

/*
x.a=1
x.b=3.140000
x.c=a
x.d=2.718000
x.e=1,2,3
x.f points to a struct of size 56 bytes
x.g=42
*/