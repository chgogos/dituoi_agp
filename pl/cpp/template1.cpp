#include <iostream>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

template <class T>
T max(T first, T second)
{
    return first > second ? first : second;
}

void test1()
{
    std::cout << "Using template" << std::endl;
    int a = 2, b = 1, c;
    char d = 'B', e = 'A', f;

    c = max(a, b);
    f = max(d, e);

    std::cout << a << " " << b << " " << c << std::endl;
    std::cout << d << " " << e << " " << f << std::endl;
}

void test2()
{
    std::cout << "Using macro" << std::endl;
    int a = 2, b = 1, c;
    char d = 'B', e = 'A', f;

    c = MAX(a, b);
    f = MAX(d, e);

    std::cout << a << " " << b << " " << c << std::endl;
    std::cout << d << " " << e << " " << f << std::endl;
}

// η test3 και η test4 παρουσιάζουν διαφορετική συμπεριφορά λόγω side-effects
void test3()
{
    std::cout << "Using template" << std::endl;
    int a = 2, b = 1, c;
    char d = 'B', e = 'A', f;

    c = max(a++, b);
    f = max(d++, e);

    std::cout << a << " " << b << " " << c << std::endl;
    std::cout << d << " " << e << " " << f << std::endl;
}

// επειδή η τιμή του a είναι μεγαλύτερη από την τιμή του b, η τιμή του a, λόγω macro, αυξάνεται 2 φορές
void test4()
{
    std::cout << "Using macro" << std::endl;
    int a = 2, b = 1, c;
    char d = 'B', e = 'A', f;

    c = MAX(a++, b);
    f = MAX(d++, e);

    std::cout << a << " " << b << " " << c << std::endl;
    std::cout << d << " " << e << " " << f << std::endl;
}

int main()
{
    test1();
    test2();
    test3();
    test4();
}

/*
Using template
2 1 2
B A B
Using macro
2 1 2
B A B
Using template
3 1 2
C A B
Using macro
4 1 3
D A C
*/