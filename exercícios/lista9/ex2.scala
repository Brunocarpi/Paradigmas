object ConversorTemperatura {
  
  def celsiusParaFahrenheit(celsius: Double): Double = {
    (celsius * 9 / 5) + 32
  }

  def main(args: Array[String]): Unit = {
    val celsius = 30.0
    val fahrenheit = celsiusParaFahrenheit(celsius)
    
    println(f"$celsius%.1f°C equivale a $fahrenheit%.1f°F")
  }
}
