#include <iostream>

using namespace std;

void fun(int x, int y = 1, int z = 2)
{
    cout << "x=" << x << " y=" << y << " z=" << z << endl;
}

int main()
{
    fun(10);
    fun(10, 20);
    fun(10, 20, 30);
}

/*
x=10 y=1 z=2
x=10 y=20 z=2
x=10 y=20 z=30
*/