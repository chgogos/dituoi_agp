#include <ncurses.h>
using namespace std;

// g++ -lncurses hello.cpp -o hello
// ./hello

int main()
{
    initscr();

    printw("Hello");

    int x = 10, y = 10;
    move(y, x);

    printw("Hi!");

    int c = getch();
    
    mvprint(0,0,"%d", c);

    getch();

    endwin();
    return 0;
}