-- Função para calcular o produto escalar de duas listas 
produtoEscalar :: Num a => [a] -> [a] -> a 
produtoEscalar xs ys = sum $ zipWith (*) xs ys 
 
-- Função para calcular a transposta de uma matriz 
transposta :: [[a]] -> [[a]] 
transposta ([]:_) = [] 
transposta x = (map head x) : transposta (map tail x) 
 
-- Função para multiplicar duas matrizes 
multiplicaMatrizes :: Num a => [[a]] -> [[a]] -> [[a]] 
multiplicaMatrizes  a  b  =  [[produtoEscalar  linha  coluna  |  coluna  <- transposta b] | linha <- a] 
 
main :: IO () 
main = do 
    let matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
    let matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]] 
     
    putStrLn "Matriz 1:" 
    mapM_ print matriz1 
    putStrLn "Matriz 2:" 
    mapM_ print matriz2 
     
    let resultado = multiplicaMatrizes matriz1 matriz2 
     
    putStrLn "Resultado da multiplicação das matrizes:" 
    mapM_ print resultado 
 
 
