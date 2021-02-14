package pl.java.simple_thread_example;
class MyThread extends Thread {
    public void run() {
        System.out.println("My thread started");
        try {
            sleep(1000 * 5);
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }
        System.out.println("My thread finished");
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        System.out.println("Main thread started");
        MyThread myTh = new MyThread();
        myTh.start();
        System.out.println("Main thread keeps working");
        myTh.join();
        System.out.println("Main thread finished");
    }
}