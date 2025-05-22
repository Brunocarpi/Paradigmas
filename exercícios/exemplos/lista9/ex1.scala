Exemplo 1 – Fatorial de 5 object CalculadoraFatorial { 
  def calcularFatorial(numero: Int): BigInt = { 
    if (numero == 0) 1 
    else (1 to numero).map(BigInt.apply).product 
  } 
 
  def main(args: Array[String]): Unit = { 
    val numero = 5 // Calculando o fatorial de 5 
 
    if (numero < 0) { 
      println("Não é possível calcular o fatorial de números negativos.") 
    } else { 
      val resultado = calcularFatorial(numero) 
      println(s"O fatorial de $numero é: $resultado") 
    } 
  } 
}