object SomaDeVectores { 
  def somarVectores(vetor1: Array[Int], vetor2: Array[Int]): Array[Int] = { 
    require(vetor1.length  ==  vetor2.length  &&  vetor1.length  ==  6,  "Os 
vetores devem ter o mesmo tamanho (6).") 
    vetor1.zip(vetor2).map { case (x, y) => x + y } 
  } 
 
  def main(args: Array[String]): Unit = { 
    val vetor1 = Array(1, 2, 3, 4, 5, 6) 
    val vetor2 = Array(6, 5, 4, 3, 2, 1) 
 
    val resultado = somarVectores(vetor1, vetor2) 
 
    println("Vetor 1: " + vetor1.mkString(", ")) 
    println("Vetor 2: " + vetor2.mkString(", ")) 
    println("Resultado da soma: " + resultado.mkString(", ")) 
  } 
}