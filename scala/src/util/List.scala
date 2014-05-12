package util

object List {
  def create(li: Array[Int]): ListNode = {
    val pre = ListNode(-1)
    var p = pre
    li.map {
      item =>
        p.next = ListNode(item)
        p = p.next
    }
    pre.next
  }

  def prettyPrint(head: ListNode) {
    head match {
      case h: ListNode =>
        print("->" + head.value)
        prettyPrint(head.next)
      case _ => return
    }
  }

  def main(args: Array[String]) {
    val head = List.create(Array(1, 2, 3, 4, 5, 6, 7, 8, 9))
    List.prettyPrint(head)
  }
}
