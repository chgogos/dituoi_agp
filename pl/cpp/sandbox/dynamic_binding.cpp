/*
Principles of Programming Languages
Gogos Christos 
DiT@UoI
2021
*/

#include <iostream>

using namespace std;

class Shape
{
public:
    virtual void draw() = 0;
};

class Circle : public Shape
{
public:
    void draw()
    {
        cout << "Circle::draw()" << endl;
    }
};

class Rectangle : public Shape
{
public:
    void draw()
    {
        cout << "Rectangle::draw()" << endl;
    }
};

class Square : public Rectangle
{
public:
    void draw()
    {
        cout << "Square::draw()" << endl;
    }
};

int main()
{
    Square *sq = new Square;
    Rectangle *rect = new Rectangle;
    Shape *ptr_shape;
    ptr_shape = sq;
    ptr_shape->draw(); // dynamic binding
    rect->draw();      // static binding
}

/*
Square::draw()
Rectangle::draw()
*/