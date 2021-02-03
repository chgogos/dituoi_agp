/*
Principles of Programming Languages
Gogos Christos 
DiT@UoI
2021
*/

// friend functions and friend classes
// H κλάση MyClass ορίζει ως φίλη συνάρτηση την ανεξάρτητη συνάρτηση fun καθώς και την κλάση A
// Αυτό σημαίνει ότι τόσο η fun όσο και η κλάση Α μπορούν να έχουν πρόσβαση σε ιδιωτικά μέλη
// των αντικειμένων της κλάσης MyClass

#include <iostream>

using namespace std;

class MyClass
{
private:
    int x;

public:
    MyClass(int x) : x(x) {}
    friend void fun();
    friend class A;
};

void fun()
{
    MyClass obj(10);
    cout << __PRETTY_FUNCTION__ << " accessing private value of a B object: " << obj.x << endl;
}

class A
{
public:
    void fun()
    {
        MyClass obj(10);
        cout << __PRETTY_FUNCTION__ << " accessing private value of a B object: " << obj.x << endl;
    }
};

int main()
{
    fun();
    A obj;
    obj.fun();
}
