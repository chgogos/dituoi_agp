#include <iostream>
using namespace std;

int g = 100; // global μεταβλητή

int main()
{
    int g = 1;           // τοπική μεταβλητή
    cout << g << endl;   // αναφορά στην τοπική μεταβλητή
    cout << ::g << endl; // αναφορά στην global μεταβλητή
}