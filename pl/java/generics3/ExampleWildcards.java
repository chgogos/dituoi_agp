import java.util.Collection;
import java.util.ArrayList;

public class ExampleWildcards {

    static void printCollection(Collection<?> c) {
        for (Object e : c) {
            System.out.println(e);
        }
    }

    public static void main(String[] args) {
        Collection<String> c = new ArrayList<String>();
        c.add("Arta");
        c.add("Ioannina");
        c.add("Preveza");
        c.add("Igoumenitsa");

        printCollection(c);
    }

}

// Arta
// Ioannina
// Preveza
// Igoumenitsa