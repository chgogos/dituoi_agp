/*
Principles of Programming Languages
Gogos Christos 
DiT@UoI
2021
*/

// object slicing

#include <iostream>

using namespace std;

class Base
{
public:
    int x;
};

class Derived : public Base
{
public:
    int y;
};

int main()
{
    Derived obj1;
    obj1.x = 10;
    obj1.y = 20;
    cout << obj1.x << " " << obj1.y << endl;

    Base obj2 = obj1; // slicing (η τιμή της μεταβλητής y δεν αντιγράφεται)
    cout << obj2.x << endl;

    Derived obj3 = *((Derived *)&obj2);
    cout << obj3.x << " " << obj3.y << endl;

    Derived obj4 = *(static_cast<Derived *>(&obj2));
    cout << obj4.x << " " << obj4.y << endl;

}

/*
10 20
10
10 10
10 10
*/
