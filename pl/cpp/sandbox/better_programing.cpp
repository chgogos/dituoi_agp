/*
Principles of Programming Languages
Gogos Christos 
DiT@UoI
2021
*/

#include <iostream>
#include <vector>
#include <list>
#include <algorithm>

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

void draw_all1(const vector<Shape *> &vs)
{
    for (int i = 0; i < vs.size(); i++)
    {
        vs[i]->draw();
    }
}

template <typename C>
void draw_all2(const C &c)
{
    typedef typename C::const_iterator CI;
    for (CI p = c.begin(); p != c.end(); p++)
    {
        (*p)->draw();
    }
}

template <typename Itr>
void draw_all3(Itr b, Itr e)
{
    for_each(b, e, mem_fun(&Shape::draw));
}

template <typename Itr>
void draw_all4(Itr b, Itr e)
{
    for_each(b, e, [](auto sh_ptr){sh_ptr->draw();});
}


int main()
{
    Circle c1;
    Rectangle r1, r2;
    vector<Shape *> vs{&c1, &r1, &r2};
    draw_all1(vs);

    cout << "#####################" << endl;

    list<Shape *> ls{&c1, &r1, &r2};
    draw_all2(vs);
    draw_all2(ls);

    cout << "#####################" << endl;

    Shape *as[]{&c1, &r1, &r2};
    draw_all3(vs.begin(), vs.end());
    draw_all3(ls.begin(), ls.end());
    draw_all3(as, as + 3);

    cout << "#####################" << endl;

    draw_all4(vs.begin(), vs.end());
    draw_all4(ls.begin(), ls.end());
    draw_all4(as, as + 3);

}

/*
Circle::draw()
Rectangle::draw()
Rectangle::draw()
#####################
Circle::draw()
Rectangle::draw()
Rectangle::draw()
Circle::draw()
Rectangle::draw()
Rectangle::draw()
#####################
Circle::draw()
Rectangle::draw()
Rectangle::draw()
Circle::draw()
Rectangle::draw()
Rectangle::draw()
Circle::draw()
Rectangle::draw()
Rectangle::draw()
#####################
Circle::draw()
Rectangle::draw()
Rectangle::draw()
Circle::draw()
Rectangle::draw()
Rectangle::draw()
Circle::draw()
Rectangle::draw()
Rectangle::draw()
*/