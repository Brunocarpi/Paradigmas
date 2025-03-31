# pip install scikit-learn
from sklearn.datasets import load_wine 
from sklearn import tree 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd 

#Base de dados
wine_data = load_wine()
X = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)
y = pd.Series(wine_data.target, name="target")

#Head de X
print("Shape de X:", X.shape)
print("\nCabeçalho de X:\n", X.head())

#Testes
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

#Árvore de decisão
dt_classifier = DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X_train, y_train)
y_pred_dt = dt_classifier.predict(X_test)

print("\nResultados - Árvore de Decisão:")
print("Matriz de Confusão:\n", confusion_matrix(y_test, y_pred_dt))
print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred_dt))

#Método KNN
knn_classifier = KNeighborsClassifier(n_neighbors=3)
knn_classifier.fit(X_train, y_train)
y_pred_knn = knn_classifier.predict(X_test)

print("\nResultados - KNN:")
print("Matriz de Confusão:\n", confusion_matrix(y_test, y_pred_knn))
print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred_knn))