import java.io.InterruptedIOException;
import java.util.concurrent.Semaphore;

class MyQueue {
    boolean active;
    int items[];
    int numberOfItems;
    int currentIndex;

    Semaphore semaphoreProducer;
    Semaphore semaphoreConsumer;

    public MyQueue(int N) {
        active = true;
        numberOfItems = N;
        items = new int[N];
        currentIndex = -1;
        semaphoreProducer = new Semaphore(N);
        semaphoreConsumer = new Semaphore(0);
    }

    void push(int value) {
        try {
            semaphoreProducer.acquire();
            System.out.printf("semaphoreProducer permits: %d\n", semaphoreProducer.availablePermits());
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }
        currentIndex++;
        items[currentIndex] = value;
        semaphoreConsumer.release();
    }

    int pop() {
        try {
            System.out.printf("semaphoreConsumer permits: %d\n", semaphoreConsumer.availablePermits());
            semaphoreConsumer.acquire();
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }
        int value = items[currentIndex];
        currentIndex--;
        if (currentIndex < 0) {
            semaphoreProducer.release();
        }
        return value;
    }

    void display() {
        System.out.print("Queue: ");
        for (int i = 0; i <= currentIndex; i++) {
            System.out.printf("%d ", items[i]);
        }
        System.out.println();
    }

    boolean isFull() {
        return currentIndex == numberOfItems - 1;
    }
}

class Producer implements Runnable {
    MyQueue q;

    public Producer(MyQueue q) {
        this.q = q;
    }

    @Override
    public void run() {
        System.out.println("Producer started");
        int i = 0;
        while (q.active) {
            try {
                Thread.sleep(300);
            } catch (InterruptedException ex) {
                ex.printStackTrace();
            }
            System.out.printf("Producer produced value %d\n", i);
            q.push(i);
            q.display();
            i++;
            if (q.isFull()) {
                q.active = false;
            }
        }
        System.out.println("Producer terminated");
    }
}

class Consumer implements Runnable {
    MyQueue q;

    public Consumer(MyQueue q) {
        this.q = q;
    }

    @Override
    public void run() {
        System.out.println("Consumer started");
        while (q.active) {
            try {
                Thread.sleep(500);
            } catch (InterruptedException ex) {
                ex.printStackTrace();
            }
            int value = q.pop();
            System.out.printf("Consumer consumed value %d\n", value);
        }
        System.out.println("Consumer terminated");
    }
}

public class Main {
    public static void main(String[] args) {
        MyQueue q = new MyQueue(10);
        Thread t1 = new Thread(new Producer(q));
        Thread t2 = new Thread(new Consumer(q));
        t1.start();
        t2.start();
        System.out.println("Consumer terminated");
    }
}