#include <stdio.h>
#include "a.h"
#include "b.h"

void fun1()
{
    printf("function fun1() declared in a.h and defined in a.c");
}

int main()
{
    fun1();
    fun2();
}