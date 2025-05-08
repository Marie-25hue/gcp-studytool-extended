import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Cargar datos
with open('dataset_ejemplo.json') as f:
    datos = pd.read_json(f)

# Preprocesamiento
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(datos['texto'])
y = datos['categoria']

# Entrenar modelo
modelo = MultinomialNB()
modelo.fit(X, y)

# Guardar modelo entrenado
joblib.dump(modelo, 'modelo_clasificador.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("✅ Modelo entrenado y guardado!")