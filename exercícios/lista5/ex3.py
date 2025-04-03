
VP = 80 #Verdadeiro Positivo
VN = 60 #Verdadeiro Negativo
FP = 30 #Falso Positivo
FN = 30 #Falso Negativo


acuracia = (VP + VN) / (VP + VN + FP + FN)
precisao = VP / (VP + FP)
recall = VP / (VP + FN)
F1_score = 2 * (precisao * recall) / (precisao + recall)


print(f"Acurácia: {acuracia:.2%}")
print(f"Precisão: {precisao:.2%}")
print(f"Recall: {recall:.2%}")
print(f"F1-Score: {F1_score:.2%}")
