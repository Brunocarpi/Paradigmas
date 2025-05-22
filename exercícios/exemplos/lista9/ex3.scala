object MultiplicacaoMatrizes { 
  def  multiplicarMatrizes(matriz1:  Array[Array[Int]],  matriz2: 
Array[Array[Int]]): Array[Array[Int]] = { 
    require(matriz1.length  ==  3  &&  matriz1(0).length  ==  3,  "A  primeira matriz deve ser 3x3.") 
    require(matriz2.length  ==  3  &&  matriz2(0).length  ==  3,  "A  segunda matriz deve ser 3x3.") 
 
    val resultado = Array.ofDim[Int](3, 3) 
 
    for (i <- 0 until 3) { 
      for (j <- 0 until 3) { 
        for (k <- 0 until 3) { 
          resultado(i)(j) += matriz1(i)(k) * matriz2(k)(j) 
        } 
      } 
    } 
 
    resultado 
  } 
 
  def main(args: Array[String]): Unit = { 
    val matriz1 = Array(Array(1, 2, 3), Array(4, 5, 6), Array(7, 8, 9)) 
    val matriz2 = Array(Array(9, 8, 7), Array(6, 5, 4), Array(3, 2, 1)) 
 
    val resultado = multiplicarMatrizes(matriz1, matriz2) 
 
    println("Matriz 1:") 
    imprimirMatriz(matriz1) 
    println("Matriz 2:") 
    imprimirMatriz(matriz2) 
    println("Resultado da multiplicação:") 
    imprimirMatriz(resultado) 
  } 
 
  def imprimirMatriz(matriz: Array[Array[Int]]): Unit = { 
    for (i <- 0 until 3) { 
      for (j <- 0 until 3) { 
        print(matriz(i)(j) + " ") 
      } 
      println() 
    } 
  } 
}