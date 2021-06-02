import java.util.*;

public class SortWithLambda {
    public static void main(String[] args) {
        List<String> cities = new ArrayList<>(List.of("arta", "ioannina", "preveza", "Igoumenitsa"));
        cities.sort((a, b) -> a.length() - b.length());
        for (String city : cities) {
            System.out.println(city);
        }
    }
}
