object SomaImpares {

  def soma(n: Int): Int = {
    if (n == 1) 1
    else (2 * n - 1) + soma(n - 1)
  }

  def main(args: Array[String]): Unit = {
    val valores = List(6, 10, 20)
    
    for (n <- valores) {
      println(s"Soma dos $n primeiros ímpares = ${soma(n)}")
    }
  }
}
