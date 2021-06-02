// 1 abstract function
interface MyFunctionalInterface {
    int fun(int x, int y);
}

class SimpleLambda {

    public static void main(String[] args) {
        MyFunctionalInterface f = (int x, int y) -> x * y;
        System.out.println(f.fun(2, 21));
    }
}

// 42