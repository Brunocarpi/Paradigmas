
VP = 50 #Verdadeiro Positivo
FN = 20 #Falso Negativo
FP = 10 #Falso Positivo
VN = 120 #Verdadeiro Negativo

acuracia = (VP + VN) / (VP + VN + FP + FN)
precisao = VP / (VP + FP)
revocacao = VP / (VP + FN)
F1_score = 2 * (precisao * revocacao) / (precisao + revocacao) 

print(f"Acurácia: {acuracia:.2%}")
print(f"Precisão: {precisao:.2%}")
print(f"Revocação: {revocacao:.2%}")
print(f"F1-Score: {F1_score:.2%}")





