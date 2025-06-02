# 📊 Predicción de Éxito en Campañas de Marketing con FastAPI y Random Forest

Este proyecto implementa una API REST usando **FastAPI** que permite predecir si una campaña de marketing será exitosa o no, en base a datos históricos y comportamiento de campañas anteriores.

Se utiliza un modelo de **Random Forest Classifier** entrenado con variables como gasto publicitario, tasas de clics, visitas al sitio web, y más.

---

> 📌 Este modelo se ha entrenado con datos reales disponibles públicamente a través de Kaggle.  
> Dataset: [Predict Conversion in Digital Marketing](https://www.kaggle.com/datasets/rabieelkharoua/predict-conversion-in-digital-marketing-dataset)
## 🧠 ¿Qué predice el modelo?

## 🔧 Tecnologías Utilizadas

- Python 3.13.3
- FastAPI
- Uvicorn
- Pandas
- Scikit-learn
- Joblib
- HTML + JavaScript (para interfaz de prueba)

---

Dado un conjunto de características de una campaña (edad del cliente, ingresos, canal de campaña, gasto publicitario, etc.), el modelo retorna:

- ✅ Si la campaña será exitosa (`True` o `False`)
- 📈 Probabilidad estimada de éxito (%)
