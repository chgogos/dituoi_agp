#include <iostream>

using namespace std;

void fun()
{
    static int x = 0;
    x++;
    cout << x << endl;
}

int main()
{
    for (int i = 0; i < 10; i++)
    {
        fun();
    }
}

/*
1
2
3
4
5
6
7
8
9
10
*/