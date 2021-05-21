#include <iostream>

using namespace std;

struct name
{
    string first;
    string last;
};

void display_full_name(name args)
{
    cout << args.first << " " << args.last << endl;
}

int main()
{
    display_full_name({.first = "John", .last = "Doe"});
}

// John Doe