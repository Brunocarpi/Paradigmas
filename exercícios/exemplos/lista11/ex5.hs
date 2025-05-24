hanoi :: Int -> String -> String -> String -> [(String, String)]
hanoi 0 _ _ _ = []
hanoi n origem auxiliar destino =
  hanoi (n - 1) origem destino auxiliar ++
  [(origem, destino)] ++
  hanoi (n - 1) auxiliar origem destino

main :: IO ()
main = do
  let movimentos = hanoi 3 "A" "B" "C"
  putStrLn "Movimentos para resolver a Torre de Hanói com 3 discos:"
  mapM_ (\(from, to) -> putStrLn $ "Mover disco de " ++ from ++ " para " ++ to) movimentos
