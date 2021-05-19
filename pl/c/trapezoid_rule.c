#include <math.h>
#include <stdio.h>
#include <stdlib.h>

double f1(double x) { return x; }
double f2(double x) { return x * x; }
double f3(double x) { return x * x * x; }

double trapezio(double a, double b, int n, double (*fp)(double)) {
  double x_i, approx;
  int i;
  double h = (b - a) / n;
  approx = (fp(a) + fp(b)) / 2.0;
  for (i = 1; i <= n - 1; i++) {
    x_i = a + i * h;
    approx += fp(x_i);
  }
  approx *= h;
  return approx;
}

int main(int argc, char **argv) {
  double global_result = 0.0;

  int n = 1000000;
  double approx;
  double a = 0.0, b = 10.0;

  approx = trapezio(a, b, n, f1);
  printf("result: %.5f\n", approx);
  approx = trapezio(a, b, n, f2);
  printf("result: %.5f\n", approx);
  approx = trapezio(a, b, n, f3);
  printf("result: %.5f\n", approx);
  approx = trapezio(a, b, n, exp);
  printf("result: %.5f\n", approx);
  approx = trapezio(a, b, n, sqrt);
  printf("result: %.5f\n", approx);

  return 0;
}

// result: 50.00000
// result: 333.33333
// result: 2500.00000
// result: 22025.46579
// result: 21.08185