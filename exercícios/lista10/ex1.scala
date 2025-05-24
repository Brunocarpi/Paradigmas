object SilhuetaEdificios {

  type Edificio = (Int, Int, Int) 

  def silhueta(edificios: List[Edificio]): List[(Int, Int)] = {
    val eventos = edificios.flatMap {
      case (e, h, d) => List((e, h), (d, -h))
    }

    val eventosOrdenados = eventos.sortBy { case (x, _) => x }

    import scala.collection.mutable

    val alturas = mutable.TreeMap[Int, Int]().withDefaultValue(0)
    alturas(0) = 1 // altura base do solo

    var alturaAnterior = 0
    var resultado = List.empty[(Int, Int)]

    for ((x, h) <- eventosOrdenados) {
      if (h > 0) alturas(h) += 1      
      else {
        if (alturas(-h) == 1) alturas -= -h
        else alturas(-h) -= 1
      }

      val alturaAtual = alturas.lastKey
      if (alturaAtual != alturaAnterior) {
        resultado = resultado :+ (x, alturaAtual)
        alturaAnterior = alturaAtual
      }
    }

    resultado
  }

  def main(args: Array[String]): Unit = {
    val edificios = List(
      (1, 11, 5), (2, 6, 7), (3, 13, 9),
      (12, 7, 16), (14, 3, 25), (19, 18, 22),
      (23, 13, 29), (24, 4, 28)
    )

    val resultado = silhueta(edificios)

    val silhuetaLinear = resultado.flatMap { case (c, a) => List(c, a) }

    println("Silhueta da cidade:")
    println(silhuetaLinear.mkString("(", ", ", ")"))
  }
}
