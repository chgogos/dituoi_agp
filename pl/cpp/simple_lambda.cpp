#include <iostream>
#include <functional>

int main()
{

    auto f = [](double x, double y)
    { return x * y; };                  // δήλωση της λάμδα συνάρτησης και ανάθεσή της σε μεταβλητή
    std::cout << f(2, 21) << std::endl; // κλήση της λάμδα συνάρτησης

    std::cout << [](double x, double y)
    { return x * y; }(3, 21)
              << std::endl; // δήλωση και άμεση κλήση της λάμδα συνάρτησης
    return 0;
}

// 42
// 63
