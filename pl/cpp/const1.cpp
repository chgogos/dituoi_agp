#include <iostream>
using namespace std;

int main()
{
    int width;
    cout << "Input width: ";
    cin >> width;

    const int result = 2 * width + 1; // δυναμική πρόσδεση τιμών σε επώνυμη σταθερά

    cout << result << endl;
}