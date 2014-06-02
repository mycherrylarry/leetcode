package datastructure;

import util.queue.ArrayListBlockingQueue;
import util.queue.BlockingQueue;

public class ProducerAndConsumerExp {
    public static class Producer<T> implements Runnable {
        private BlockingQueue<T> bq;
        private final T product;

        Producer(BlockingQueue<T> bq, T p) {
            this.bq = bq;
            this.product = p;
        }

        public void run() {
            try {
                while (true) {
                    bq.put(product);
                    System.out.println("produce");
                }
            } catch (InterruptedException ex) {
                System.out.println("exp");
            }
        }
    }

    public static class Consumer<T> implements Runnable {

        private BlockingQueue<T> bq;

        Consumer(BlockingQueue<T> bq) {
            this.bq = bq;
        }

        public void run() {
            try {
                while (true) {
                    bq.take();
                    System.out.println("consume");
                }
            } catch (InterruptedException ex) {
                System.out.println("exp");
            }
        }

    }

    public static void main(String[] args) {
        BlockingQueue<String> bq = new ArrayListBlockingQueue<String>(100);
        Producer<String> producer = new Producer<String>(bq, "item");
        Consumer<String> consumer = new Consumer<String>(bq);
        new Thread(producer).start();
        new Thread(consumer).start();
    }
}
