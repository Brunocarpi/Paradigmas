-- Função auxiliar para verificar se uma substring está presente em uma determinada posição da string 
verificarSubString :: String -> String -> Int -> Bool 
verificarSubString [] _ _ = True 
verificarSubString _ [] _ = False 
verificarSubString (x:xs) (y:ys) pos 
    | x == y = verificarSubString xs ys (pos + 1) 
    | otherwise = False 
 
-- Função principal para encontrar a posição da substring "fofo" na string 
posicaoSubString :: String -> Int -> Maybe Int 
posicaoSubString [] _ = Nothing 
posicaoSubString str pos 
    | verificarSubString "fofo" str pos = Just pos 
    | otherwise = posicaoSubString (tail str) (pos + 1) 
 
main :: IO () 
main = do 
    let stringOriginal = "Gatossaoosanimaismaisfofosdaterra" 
    let posicao = posicaoSubString stringOriginal 0 
    case posicao of 
        Just p -> putStrLn $ "A substring 'fofo' está na posição " ++ show p ++ " da string." 
        Nothing -> putStrLn "A substring 'fofo' não foi encontrada na string."