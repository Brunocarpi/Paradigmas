from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report  
 
iris = load_iris() 
X = iris.data 
y = iris.target 
 
(X_train, X_test, y_train, y_test) = train_test_split(X,y) 
 

modelo = KNeighborsClassifier()  
modelo.fit(X_train,y_train) 
acuracia = str(round(modelo.score(X_test,y_test) * 100, 2))+"%" 
y_pred = modelo.predict(X_test) 
 

print("A acurácia do modelo KNN foi",acuracia) 
print(classification_report(y_test, y_pred))