#include <iostream>

using namespace std;

void fun(float b = 0.0)
{
    cout << "Calling function fun(float)" << endl;
}

void fun()
{
    cout << "Calling function fun()" << endl;
}

int main()
{
    fun(1.5); // ok
    // fun(); // error: call of overloaded 'fun()' is ambiguous
}