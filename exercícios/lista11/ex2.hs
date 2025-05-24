celsiusParaFahrenheit :: Float -> Float
celsiusParaFahrenheit c = (c * 9 / 5) + 32

main :: IO ()
main = do
  let celsius = 30.0
  let fahrenheit = celsiusParaFahrenheit celsius
  putStrLn ("Temperatura em Celsius: " ++ show celsius ++ "°C")
  putStrLn ("Temperatura em Fahrenheit: " ++ show fahrenheit ++ "°F")
