object Esfera {

  def calcularVolume(raio: Double): Double = {
    val pi = 3.0
    (4.0 / 3.0) * pi * math.pow(raio, 3)
  }

  def calcularAreaSuperficie(raio: Double): Double = {
    val pi = 3.0
    4 * pi * math.pow(raio, 2)
  }

  def main(args: Array[String]): Unit = {
    val raio = 6.0

    val volume = calcularVolume(raio)
    val area = calcularAreaSuperficie(raio)

    println(f"Raio: $raio%.1f cm")
    println(f"Volume da esfera: $volume%.2f cm³")
    println(f"Área da superfície da esfera: $area%.2f cm²")
  }
}
