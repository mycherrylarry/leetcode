/**
 * Created by le.chang on 2014/07/04.
 */
public enum Currency {
    PENNY(1), NICKLE(6);
    private int value;
    private Currency(int value) {
        this.value = value;
    }

    public static void main(String[] args) {
        Currency c = Currency.PENNY;
        System.out.println(c);

    }
}
