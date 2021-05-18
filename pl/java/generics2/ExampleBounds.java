import java.util.Arrays;   
import java.util.Collections;

public class ExampleBounds {

    public static <T extends Comparable> void doIt(T[] list) {
        Arrays.sort(list, Collections.reverseOrder());
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

        // MyClass c[] = new MyClass[] { new MyClass(1), new MyClass(2), new MyClass(3) };
        // doIt(c); // error: method doIt in class Example cannot be applied to given types;
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
