#include <iostream>

using namespace std;

void foo(int x)
{
    cout << "int " << x << endl;
}

void foo(float x)
{
    cout << "float " << x << endl;
}

void foo(int x, float y, char z)
{
    cout << "another overloaded function" << endl;
}

int main()
{
    foo(4);
    foo(4.5f);
    foo(45, 6.7f, 'a');
}