#include <stdio.h>
#include "a.h"
#include "b.h"


void fun1()
{
    printf("function fun1() declared in a.h and defined in a.c\n");
}

int main()
{
    printf("Executable started\n");
    fun1();
    fun2();
    printf("Executable finished\n");
}
