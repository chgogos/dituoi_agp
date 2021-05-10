#include <stdio.h>

square(x,n)
int x,n;
{
    int i, p;
    p = 1;
    for(i = 1;i<=n;++i) p = p * x;

    return (p);
}

int main(){
    int r = square(2,10);
    printf("%d\n", r);
}