#include <iostream>

using namespace std;

// x μεταβίβαση κατά τιμή
// y μεταβίβαση κατά αναφορά
// z μεταβίβαση κατά αναφορά (μονόδρομη)
void fun1(int x, int &y, const int &z)
{
    x++;
    y++;
    // z++; // error: increment of read-only reference 'z'
    cout << "fun1: x=" << x << " y=" << y << " z=" << z << endl;
}

int main()
{
    int a = 1, b = 1, c = 1;
    fun1(a, b, c);
    cout << "main: a=" << a << " b=" << b << " c=" << c << endl;
}

/*
fun1: x=2 y=2 z=1
main: a=1 b=2 c=1
*/