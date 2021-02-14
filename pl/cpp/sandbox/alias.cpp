#include <iostream>

int main(){
    int x = 10;
    int &y=x;

    y =20;

    std::cout << "x=" << x << std::endl;
    std::cout << "y=" << y << std::endl;
}

/*
x=20
y=20
*/