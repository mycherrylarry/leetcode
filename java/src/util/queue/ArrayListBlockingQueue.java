package util.queue;

import java.util.ArrayList;

public class ArrayListBlockingQueue<T> implements BlockingQueue<T> {
    private ArrayList<T> queue;
    private final int capacity;

    public ArrayListBlockingQueue(int c) {
        capacity = c;
        queue = new ArrayList<T>();
    }

    public synchronized void put(T t) throws InterruptedException {
        while (queue.size() == capacity) {
            wait();
        }
        queue.add(t);
        notify();
    }

    public synchronized T take() throws InterruptedException {
        while (queue.isEmpty()) {
            wait();
        }
        T item = queue.remove(queue.size() - 1);
        notify();
        return item;
    }
}
