# 🧠 Clasificador de Texto - PoC en Desarrollo

## ✍️ Descripción 

Este proyecto está en construcción.  
No es un producto final ni una demo cerrada.  
Es un espacio de aprendizaje técnico real, donde:

- Se explora cómo se entrena un modelo básico de Machine Learning  
- Se construye una API REST funcional con FastAPI para exponer el modelo  
- Se sientan las bases para implementar estos conceptos en plataformas como Vertex AI y Hugging Face Spaces  
- Se desarrolla pensamiento técnico independiente y aplicabilidad práctica  

---

## 🧭 Objetivo principal del proyecto

Este prototipo fue creado para:

- Aprender a entrenar modelos supervisados de Machine Learning aplicados a texto  
- Comprender cómo se clasifican datos y se transforman en predicciones útiles  
- Experimentar con el ciclo completo: datos → vectorización → entrenamiento → API  
- Simular de forma local lo que luego puede desplegarse en Vertex AI o BigQuery ML  
- Aplicar IA a procesos educativos con trazabilidad, precisión y ética  

---

## 🎓 Enfoque pedagógico

El proyecto tiene como objetivo convertirse en un sistema que permita:

- Clasificar errores en categorías como: conceptual, operativo, distractor  
- Sugerir acciones pedagógicas adaptadas: revisión técnica, práctica dirigida o apoyo conceptual  
- Generar feedback basado en datos reales y evitar alucinaciones típicas de modelos genéricos  
- Desarrollar soluciones IA con foco en: ética, precisión, trazabilidad y aplicabilidad pedagógica  

---

## ⚙️ Estructura del proyecto

- `dataset_ejemplo.json`: Mini dataset de prueba  
- `entrenador_clasificador.py`: Script de entrenamiento  
- `api_fastapi.py`: API REST para predicciones  
- `requirements.txt`: Librerías necesarias  
- `.gitignore`: Archivos a excluir del repo  
- `README.md`: Este archivo  

---

## 🚀 ¿Qué hace este prototipo?

**Actualmente:**

- Entrena un modelo Naive Bayes con scikit-learn sobre textos positivos/negativos  
- Vectoriza los textos con CountVectorizer  
- Expone un endpoint `POST /clasificar` para hacer predicciones vía API  

**A futuro:**

- Incorporar clasificadores más avanzados  
- Usar embeddings con Hugging Face (como DistilBERT)  
- Entrenar y desplegar modelos en Vertex AI o BigQuery ML  

---

## 🔬 ¿Cómo testear el modelo entrenado?

Después de entrenar el modelo con:


---

python ml/entrenador_clasificador.py


Se puede validar en consola con este test rápido:

```python
import joblib
modelo = joblib.load("modelo_clasificador.pkl")
vectorizer = joblib.load("vectorizer.pkl")
texto = "odio los lunes"
vector = vectorizer.transform([texto])
print(modelo.predict(vector))

---

🧪 Instrucciones de uso

1. Instalar dependencias

pip install -r ml/requirements.txt

---

2. Entrenar el modelo

python ml/entrenador_clasificador.py

---

3. Levantar la API

python ml/api_fastapi.py

---

4. Probar vía curl

curl -X POST http://localhost:8000/clasificar -H "Content-Type: application/json" -d '{"texto":"me encanta programar"}'

---

📌 Estado actual del proyecto
En desarrollo activo

- Entrenamiento inicial funcionando
- API local operativa
- Métricas de validación
- Dataset ampliado
- Embeddings y modelos Hugging Face
- Entrenamiento en Vertex AI

---

🧠 Relación con la certificación GCP Professional Data Engineer
Este proyecto aplica conceptos clave del examen:

- Diseño de pipelines de datos
- Entrenamiento y evaluación de modelos predictivos
- Implementación de APIs para consumo de modelos
- Versionado y flujo reproducible
- Preparación para escalar a servicios como Vertex AI, BigQuery ML y Cloud Run

---

🙋‍♂️ ¿Colaboración?
El proyecto está abierto a contribuciones técnicas, sugerencias y mejoras.
Cualquier persona interesada en IA aplicada, educación o arquitectura de datos puede participar mediante Pull Requests o issues.

