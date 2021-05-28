public class Example {

    public static <T> void doIt(T[] list) {
        for (T elem : list) {
            System.out.println(elem);
        }
    }

    public static void main(String[] args) {
        Integer a[] = new Integer[] { 1, 2, 3, 4, 5 };
        doIt(a);

        System.out.println();

        String b[] = new String[] { "Arta", "Ioannina", "Preveza", "Igoumenitsa" };
        doIt(b);

        System.out.println();

        MyClass c[] = new MyClass[] { new MyClass(1), new MyClass(2), new MyClass(3) };
        doIt(c);
    }
}

class MyClass {
    private int x;

    public MyClass(int x) {
        this.x = x;
    }

    public String toString() {
        return String.format("Object:%d value: %d", this.hashCode(), x);
    }

}

// 1
// 2
// 3
// 4
// 5

// Arta
// Ioannina
// Preveza
// Igoumenitsa

// Object:617901222 value: 1
// Object:1149319664 value: 2
// Object:2093631819 value: 3