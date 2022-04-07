all: app.exe

app.exe: a.o b.o
	gcc a.o b.o -o app.exe

a.o: a.c a.h
	gcc -o a.o -c a.c

b.o: b.c b.h
	gcc -o b.o -c b.c

clean:
	rm *.o app.exe