#include <iostream>

using namespace std;

struct name
{
    string first;
    string last;
};

int main()
{
    struct name r1 = {"John", "Doe"};
    struct name r2 = {.first = "John", .last = "Doe"};
    struct name r3 = {.first = "John", "Doe"};
    struct name r4 = {"John", .last = "Doe"};

    cout << r1.first << " " << r1.last << endl;
    cout << r2.first << " " << r2.last << endl;
    cout << r3.first << " " << r3.last << endl;
    cout << r4.first << " " << r4.last << endl;
}

// John Doe
// John Doe
// John Doe
// John Doe