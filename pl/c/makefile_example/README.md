# Απλό παράδειγμα με makefile

```
$ make
gcc -o a.o -c a.c
gcc -o b.o -c b.c
gcc a.o b.o -o app.exe
$ ./app.exe
Executable started
function fun1() declared in a.h and defined in a.c
function fun2() declared in b.h and defined in b.c
Executable finished
```

## Tutorials

* https://makefiletutorial.com/
* https://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/
* https://www.cs.swarthmore.edu/~newhall/unixhelp/howto_makefiles.html