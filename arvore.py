from sklearn.datasets import load_iris #importa a biblioteca de dados da flor iris
from sklearn import tree 
from sklearn.model_selection import train_test_split #define a proporção de dados para o teste
import pandas as pd #importa a biblioteca do pandas
import sklearn.metrics as metrics #importa as métricas de avaliação


iris = load_iris()


X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25)
clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3) #ajusta a proporção de decisão tomada pela árvore de teste
clf = clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

print(iris['DESCR'])
print("\nMatriz de confusão detalhada:\n",
 pd.crosstab(y_test, predictions, rownames=['Real'], colnames=['Predito'], margins=True, margins_name='Todos'))
print("Relatório sobre a qualidade:\n")
print(metrics.classification_report(y_test, predictions, target_names=['Setosa', 'Versicolor', 'Virgínica']))