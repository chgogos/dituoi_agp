#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<string> cities{"arta", "ioannina", "preveza", "Igoumenitsa"};
    sort(cities.begin(), cities.end(), [](auto a, auto b)
         { return a.length() < b.length(); });
    for (auto city : cities)
    {
        cout << city << endl;
    }
}

// arta
// preveza
// ioannina
// Igoumenitsa