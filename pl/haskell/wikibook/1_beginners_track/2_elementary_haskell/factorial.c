#include <stdio.h>

int factorial(int n)
{
    int res = 1;
    for (; n > 1; n--)
        res *= n;
    return res;
}

int main()
{
    int f = factorial(10);
    printf("%d\n", f);
}