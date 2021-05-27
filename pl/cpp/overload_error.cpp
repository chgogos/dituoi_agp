#include <iostream>

int fun(int x)
{
    // dummy
    return 0;
}

float fun(int x) //  error: ambiguating new declaration of 'float fun(int)'
{
    // dummy
    return 0.0;
}

int main() {}