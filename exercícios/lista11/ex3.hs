soma :: Int -> Int
soma 1 = 1
soma n = (2 * n - 1) + soma (n - 1)

main :: IO ()
main = do
  let n1 = 6
  let n2 = 10
  let n3 = 20

  putStrLn $ "Soma dos " ++ show n1 ++ " primeiros ímpares: " ++ show (soma n1)
  putStrLn $ "Soma dos " ++ show n2 ++ " primeiros ímpares: " ++ show (soma n2)
  putStrLn $ "Soma dos " ++ show n3 ++ " primeiros ímpares: " ++ show (soma n3)
