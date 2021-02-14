/*
Μολονότι η C διαθέτει 2 είδη δομημένων τύπων δεδομένων, τις διατάξεις και τις εγγραφές (struct), 
οι εγγραφές μπορούν να επιστρέφονται από συναρτήσεις αλλά όχι οι διατάξεις. 
Ωστόσο, θα πρέπει να σημειωθεί ότι η C επιτρέπει την επιστροφή ενός δείκτη προς μια διάταξη.
*/

#include <stdio.h>
#include <stdlib.h>

struct my_struct{
    int a;
    int b;
};

// επιστροφή εγγραφής από συνάρτηση
struct my_struct fun1(int a, int b){
    struct my_struct x;
    x.a=a;
    x.b=b;
    return x;
}

// μια συνάρτηση δεν μπορεί να επιστρέφει μια διάταξη
// int[10] fun2(){
//     // ...
// }

// επιστροφή ενός δείκτη προς διάταξη n ακεραίων 
int* fun3(int v, int n){
    int *a= (int*)malloc(sizeof(int)*n);
    for(int i=0;i<n;i++){
        a[i]=v;
    }
    return a;
}

int main(){
    printf("1. Function returns struct\n");
    struct my_struct r = fun1(1,2);
    printf("%d %d\n", r.a, r.b);

    printf("2. Function returns array (through a pointer)\n");
    int *a=fun3(42, 5);
    for(int i=0;i<5;i++){
        printf("a[%d]=%d\n", i, a[i]);
    }
    free(a);
}

/*
1. Function returns struct
1 2
2. Function returns array (through a pointer)
a[0]=42
a[1]=42
a[2]=42
a[3]=42
a[4]=42
*/