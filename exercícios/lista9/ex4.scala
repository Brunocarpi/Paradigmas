object VerificaPalindromo {

  def ehPalindroma(lista: List[Int]): Boolean = {
    lista == lista.reverse
  }

  def main(args: Array[String]): Unit = {

    val lista1 = List(1, 2, 3, 2, 1)
    val lista2 = List(5, 3, 2, 1)

    if (ehPalindroma(lista1))
      println(s"Lista 1: $lista1 => A lista é palíndroma!")
    else
      println(s"Lista 1: $lista1 => A lista NÃO é palíndroma.")

    if (ehPalindroma(lista2))
      println(s"Lista 2: $lista2 => A lista é palíndroma!")
    else
      println(s"Lista 2: $lista2 => A lista NÃO é palíndroma.")
  }
}
