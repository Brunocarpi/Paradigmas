import pandas as pd 
 
from sklearn.datasets import load_breast_cancer 
from sklearn.metrics import confusion_matrix, classification_report 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split

cancer_mama = load_breast_cancer() 
X = pd.DataFrame(cancer_mama.data, columns=cancer_mama.feature_names) 
y = pd.Categorical.from_codes(cancer_mama.target, cancer_mama.target_names)
y = pd.get_dummies(y, drop_first=True) 
# A função get_dummies() substitui as possíveis classificações (classes) 
# por um valor numérico. Neste caso, malignant = 0 e benign = 1 

X_train, X_test, y_train, y_test = train_test_split(X, y, 
random_state=1) 
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean') 
knn.fit(X_train, y_train)
# y_pred = Previsões realizadas pelo algoritmo 
y_pred = knn.predict(X_test)



print(y) 
print(y_pred)
print(X.shape) 
print(X.head())
# Retorna a matriz de confusão mostrando os acertos e erros da nossa previsão 
print(confusion_matrix(y_test, y_pred)) 
# Retorna o relatório de classificação, apontando: 
# acurácia, precisão, revocação e F1. 
print(classification_report(y_test, y_pred, target_names=['Maligno', 'Benigno']))
