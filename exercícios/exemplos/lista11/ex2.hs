somaVetores :: [Int] -> [Int] -> [Int] 
somaVetores [] [] = [] 
somaVetores (x:xs) (y:ys) = (x + y) : somaVetores xs ys 
 
main :: IO () 
main = do 
    putStrLn "Digite os elementos do primeiro vetor separados por espaço:" 
    input1 <- getLine 
    let vetor1 = map read $ words input1 :: [Int] 
 
    putStrLn "Digite os elementos do segundo vetor separados por espaço:" 
    input2 <- getLine 
    let vetor2 = map read $ words input2 :: [Int] 
 
    if length vetor1 /= 6 || length vetor2 /= 6 
        then putStrLn "Os vetores devem ter tamanho 6!" 
        else do 
            let resultado = somaVetores vetor1 vetor2 
            putStrLn $ "A soma dos vetores é: " ++ show resultado 
 
 
 
