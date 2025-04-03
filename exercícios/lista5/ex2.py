
VP = 50 #Verdadeiro Positivo
VN = 120 #Verdadeiro Negativo
FN = 20 #Falso Negativo
FP = 10 #Falso Positivo


acuracia = (VP + VN) / (VP + VN + FP + FN)
precisao = VP / (VP + FP)
recall = VP / (VP + FN)
F1_score = 2 * (precisao * recall) / (precisao + recall)


print(f"Acurácia: {acuracia:.2%}")
print(f"Precisão: {precisao:.2%}")
print(f"Recall: {recall:.2%}")
print(f"F1-Score: {F1_score:.2%}")
