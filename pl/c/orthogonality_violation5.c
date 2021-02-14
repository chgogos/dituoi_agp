/*
Εξάρτηση από τα συμφραζόμενα για τον τελεστή + στην έκφραση a + b. 
Αν το a είναι δείκτης προς μια τιμή float που καταλαμβάνει 4 bytes τότε η τιμή του b θα πολλαπλασιαστεί επί 4 πριν προστεθεί στο a.
*/

#include <stdio.h>

void fun1(){
    int a = 0;
    int b = 4;
    a = a+b;
    printf("%d\n", a);
}

void fun2(){
    float array[5]={1.1,1.2,1.3,1.4,1.5};
    float *a=array;
    printf("%zd %f\n", a, *a);

    int b=4;
    a = a+b;
    printf("%zd %f\n", a, *a);
}

int main(){
    fun1();
    fun2();
}

/*
4
6684112 1.100000
6684128 1.500000
*/