package util;

public class List {
    public static ListNode create(int[] li) {
        ListNode pre = new ListNode(-1);
        ListNode p = pre;
        for (int i = 0; i < li.length; i++) {
            p.next = new ListNode(li[i]);
            p = p.next;
        }
        return pre.next;
    }

    public static void prettyPrint(ListNode head) {
        ListNode p = head;
        while (p != null) {
            System.out.print("->");
            System.out.print(p.val);
            p = p.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        ListNode head = List.create(new int[]{1, 2, 3, 4, 5});
        List.prettyPrint(head);
    }
}
