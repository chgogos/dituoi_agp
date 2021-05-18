class Example1 {

    static void fun(int mat[][]) {
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j++) {
                System.out.format("%3d", mat[i][j]);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int a[][] = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
        fun(a);

        System.out.println();

        int b[][] = { { 1, 2 }, { 3, 4 }, { 5, 6 }, { 7, 8 } };
        fun(b);
    }
}

// 1 2 3
// 4 5 6
// 7 8 9

// 1 2
// 3 4
// 5 6
// 7 8
