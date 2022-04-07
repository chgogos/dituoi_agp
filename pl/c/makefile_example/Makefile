all: app.exe

app.exe: a.o b.o
	gcc -o app.exe a.o b.o

a.o: a.c a.h
	gcc -o a.o -c a.c

b.o: b.c a.h
	gcc -o b.o -c b.c

clean:
	rm *.o app.exe