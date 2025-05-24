volumeEsfera :: Float -> Float
volumeEsfera r = (4 / 3) * piAprox * r^3
  where piAprox = 3.0

areaSuperficieEsfera :: Float -> Float
areaSuperficieEsfera r = 4 * piAprox * r^2
  where piAprox = 3.0

main :: IO ()
main = do
  let raio = 6.0
  let volume = volumeEsfera raio
  let area = areaSuperficieEsfera raio

  putStrLn ("Raio: " ++ show raio ++ " cm")
  putStrLn ("Volume da esfera: " ++ show volume ++ " cm³")
  putStrLn ("Área da superfície da esfera: " ++ show area ++ " cm²")
