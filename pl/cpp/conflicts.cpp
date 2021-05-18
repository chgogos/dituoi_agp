#include <iostream>

using namespace std;

void fun(int &first, int &second)
{
    cout << "&first = " << &first << endl;
    cout << "&second = " << &second << endl;
    first++;
    second--;
}

int main()
{
    int x = 1;
    fun(x, x); // τα first και second γίνονται ψευδώνυμα στη συνάρτηση fun
    cout << x << endl;
}

// &first = 0x7afe1c 
// &second = 0x7afe1c
// 1