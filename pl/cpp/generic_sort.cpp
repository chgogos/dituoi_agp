#include <iostream>

using namespace std;

template <class Type>
void generic_sort(Type list[], int len)
{
    int top, bottom;
    Type temp;
    for (top = 0; top < len - 2; top++)
        for (bottom = top + 1; bottom < len - 1; bottom++)
            if (list[top] > list[bottom])
            {
                temp = list[top];
                list[top] = list[bottom];
                list[bottom] = temp;
            }
}

int main()
{
    int a[] = {3, 2, 1, 4, 5};
    generic_sort(a, 5);
    for (int i = 0; i < 5; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;

    int b[] = {'b', 'e', 'c', 'a', 'd', 'f'};
    generic_sort(b, 6);
    for (int i = 0; i < 6; i++)
    {
        cout << (char)b[i] << " ";
    }
    cout << endl;
}

/*
1 2 3 4 5 
a b c d e f
*/