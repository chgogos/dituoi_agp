public class Example1 {
    public static void foo(int x) {
        x++;
    }

    public static void bar(MyClass obj) {
        obj.a++;
    }

    public static void main(String[] args) {
        int x = 5;
        // κλήση με τιμή
        foo(x);
        System.out.println(x);

        MyClass obj = new MyClass(5);
        // προσομοίωση κλήσης με αναφορά
        bar(obj);
        System.out.println(obj.a);
    }

}

class MyClass {
    public int a;

    public MyClass(int a) {
        this.a = a;
    }
}