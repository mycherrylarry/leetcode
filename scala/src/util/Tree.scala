package util

object Tree {
  def create(li: Array[Int]): TreeNode = li.length match {
    case 0 => null
    case _ =>
      val mid: Int = li.length / 2
      val root: TreeNode = TreeNode(li(mid))
      root.left = Tree.create(li.slice(0, mid))
      root.right = Tree.create(li.slice(mid + 1, li.length))
      root
  }

  def prettyPrint(root: TreeNode, level: Int = 0) {
    if (root == null) return
    Tree.prettyPrint(root.right, level + 1)
    print("==" * level)
    println(root.value)
    Tree.prettyPrint(root.left, level + 1)
  }

  def main(args: Array[String]) {
    val root = Tree.create(Array(1, 2, 3, 4, 5, 6, 7, 8, 9))
    Tree.prettyPrint(root)
  }
}
