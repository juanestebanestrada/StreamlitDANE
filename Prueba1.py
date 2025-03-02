import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Agricultural Price Forecasting", page_icon="🌾", layout="wide")

# Título de la presentación
st.title("🌾 Agricultural Product Price Forecasting Methods: A Review")
st.markdown("---")

# Sección de Resumen
st.header("📝 Resumen")
st.write("""
El artículo revisa los métodos de predicción de precios de productos agrícolas, explorando métodos tradicionales, métodos inteligentes y métodos de modelos combinados. 
Se discuten los desafíos actuales en la predicción de precios de productos agrícolas y se concluye que el uso de modelos combinados es una tendencia futura. 
Además, se destaca la importancia de integrar datos estructurados y no estructurados en los modelos de predicción y la necesidad de garantizar tanto la precisión de los valores como la dirección de las tendencias en las predicciones.
""")
st.markdown("---")

# Sección de Introducción
st.header("📖 Introducción")
st.write("""
La predicción de precios agrícolas es crucial para la estabilidad económica y la seguridad alimentaria global. Los precios agrícolas están influenciados por factores complejos y muestran fluctuaciones irregulares. 
Este artículo revisa los métodos de predicción de precios agrícolas, desde los métodos tradicionales hasta los métodos inteligentes y los modelos combinados, con el objetivo de proporcionar una visión general del desarrollo de este campo y discutir las tendencias futuras.
""")
st.markdown("---")

# Sección de Referencias Literarias
st.header("📚 Referencias Literarias")
st.write("""
El artículo cita numerosos estudios previos que han abordado la predicción de precios agrícolas, incluyendo métodos de regresión, modelos de series temporales, y métodos de aprendizaje automático. Algunas referencias clave incluyen:
- **Moore (1917)**: Sobre el uso de modelos de regresión lineal múltiple.
- **Ma et al. (2012)**: Sobre la predicción de precios de cerdos utilizando modelos VAR.
- **Kohzadi et al. (1996)**: Sobre el uso de redes neuronales para predecir precios de productos agrícolas.
""")
st.markdown("---")

# Sección del Problema
st.header("❓ Problema")
st.write("""
La predicción de precios agrícolas es un desafío debido a la complejidad de los factores que influyen en los precios, como la oferta y la demanda, el clima, las políticas y el entorno del mercado internacional. 
Los métodos tradicionales tienen limitaciones en la predicción de datos no lineales y no estacionarios, mientras que los métodos inteligentes requieren grandes cantidades de datos y recursos computacionales.
""")
st.markdown("---")

# Sección de la Solución
st.header("💡 Solución")
st.write("""
El artículo propone el uso de modelos combinados que integren diferentes métodos de predicción para mejorar la precisión. 
También sugiere la integración de datos estructurados y no estructurados en los modelos de predicción y la necesidad de garantizar tanto la precisión de los valores como la dirección de las tendencias en las predicciones.
""")
st.markdown("---")

# Sección de Conclusiones
st.header("📌 Conclusiones")
st.write("""
1. **El uso de modelos combinados es una tendencia futura en la predicción de precios agrícolas.**
2. **La integración de datos estructurados y no estructurados en los modelos de predicción es crucial.**
3. **Es importante garantizar tanto la precisión de los valores como la dirección de las tendencias en las predicciones.**
4. **Se necesitan más investigaciones sobre la extracción y cuantificación de datos no estructurados, métodos de integración de modelos combinados, y estrategias de combinación de múltiples escalas de tiempo.**
""")
st.markdown("---")

# Sección de Referencias
st.header("📖 Referencias")
st.write("""
El artículo incluye una extensa lista de referencias que respaldan los métodos y conclusiones presentados. Algunas de las referencias clave son:
- **Bates, J.M.; Granger, C.W.J.** The combination of forecasts. *Oper. Res. Soc.* 1969, 20, 451–468.
- **Kohzadi, N.; Boyd, M.S.; Kermanshahi, B.; Kaastra, I.** A comparison of artificial neural network and time series models for forecasting commodity prices. *Neurocomputing* 1996, 10, 169–181.
- **Ma, Z.** Prediction of Hog Price and Produce Based on Dynamic Bayesian Network. *Master’s Thesis*, Huazhong Agricultural University, Wuhan, China, 2019.
- **Liakos, K.G.; Busato, P.; Moshou, D.; Pearson, S.; Bochtis, D.** Machine learning in agriculture: A review. *Sensors* 2018, 18, 2674.
""")
st.markdown("---")



import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Agricultural Price Prediction", page_icon="🌾", layout="wide")

# Título de la presentación
st.title("🌾 Agricultural Products Price Prediction Based on Improved RBF Neural Network Model")
st.markdown("---")

# Sección de Resumen
st.header("📝 Resumen")
st.write("""
El artículo aborda la predicción de precios de productos agrícolas utilizando un modelo mejorado de red neuronal de función de base radial (RBF). 
Se analizan los factores que influyen en los precios de los productos agrícolas, como la oferta y la demanda, los costos actuales, los impactos políticos y otros factores. 
El estudio utiliza datos históricos de precios de productos como el ajo y el cerdo en China para entrenar el modelo RBF y predecir futuras fluctuaciones de precios. 
El modelo RBF mejorado muestra una alta precisión en la predicción de precios, superando los métodos tradicionales de predicción. 
El artículo concluye que la predicción precisa de los precios agrícolas es crucial para la estabilidad económica y la seguridad alimentaria.
""")
st.markdown("---")

# Sección de Introducción
st.header("📖 Introducción")
st.write("""
La predicción de tendencias de precios es un elemento técnico crucial en el proceso de toma de decisiones en el mercado. 
Tradicionalmente, los métodos de predicción de precios se basaban en investigaciones de campo y análisis estadísticos manuales, lo que resultaba en costos elevados y errores potenciales. 
Con el avance de la tecnología, los métodos basados en minería de datos y redes neuronales han ganado popularidad. 
Este artículo propone un modelo mejorado de red neuronal RBF para predecir los precios de productos agrícolas, utilizando datos históricos y factores de influencia como la oferta, la demanda y los costos de producción.
""")
st.markdown("---")

# Sección de Referencias Literarias
st.header("📚 Referencias Literarias")
st.write("""
El artículo cita varios estudios previos que han abordado la predicción de precios de productos agrícolas y el uso de redes neuronales en la predicción de tendencias de mercado. Algunas referencias clave incluyen:
- **Chen et al. (2019)**: Sobre la predicción de tendencias de precios utilizando métodos de minería de datos.
- **Cheng et al. (2016)**: Sobre el uso de redes neuronales en la predicción de precios.
- **Jia et al. (2022)**: Sobre la aplicación de técnicas de minería de datos en la predicción de precios agrícolas.
""")
st.markdown("---")

# Sección del Problema
st.header("❓ Problema")
st.write("""
La fluctuación de los precios de los productos agrícolas es un problema significativo que afecta la estabilidad económica y la seguridad alimentaria. 
Los métodos tradicionales de predicción de precios son costosos, propensos a errores y no pueden manejar grandes volúmenes de datos. 
Además, los factores que influyen en los precios agrícolas son complejos y dinámicos, lo que dificulta la predicción precisa utilizando métodos convencionales.
""")
st.markdown("---")

# Sección de la Solución
st.header("💡 Solución")
st.write("""
El artículo propone un modelo mejorado de red neuronal RBF para predecir los precios de productos agrícolas. 
Este modelo utiliza datos históricos y factores de influencia como la oferta, la demanda, los costos de producción y los impactos políticos para entrenar la red neuronal. 
El modelo RBF mejorado es capaz de manejar grandes volúmenes de datos y proporcionar predicciones precisas, superando los métodos tradicionales de predicción.
""")
st.markdown("---")

# Sección de Conclusiones
st.header("📌 Conclusiones")
st.write("""
1. **El modelo mejorado de red neuronal RBF es efectivo para predecir los precios de productos agrícolas, mostrando una alta precisión en las predicciones.**
2. **Los principales factores que influyen en la fluctuación de los precios de los productos agrícolas son la oferta, la demanda, los costos de producción y los impactos políticos.**
3. **La predicción precisa de los precios agrícolas es crucial para la estabilidad económica y la seguridad alimentaria.**
4. **El modelo RBF mejorado puede eliminar la necesidad de estadísticas manuales complejas y proporcionar predicciones más rápidas y precisas.**
""")
st.markdown("---")

# Sección de Referencias
st.header("📖 Referencias")
st.write("""
El artículo incluye una extensa lista de referencias que respaldan los métodos y conclusiones presentados. Algunas de las referencias clave son:
- **Chen, W., F. Cai, H. Chen, and M. De Rijke.** Joint neural collaborative filtering for recommender systems. *ACM Transactions on Information Systems* 37 (4):1–30. doi:10.1145/3343117.
- **Cheng, H.T., L. Koc, J. Harmsen, T. Shaked, T. Chandra, H. Aradhye, G. Anderson, G. Corrado, W. Chai, and M. Ispir.** Wide & deep learning for recommender systems. *Proceedings of the 1st workshop on deep learning for recommender systems*. Boston, MA, USA.
- **Jia, H., S. Shen, J. Alberto Ramirez Garcia, and C. Shi.** Partner with a third-party delivery service or not? A prediction-and-decision tool for restaurants facing takeout demand surges during a pandemic. *Service Science* 14 (2):139–55. doi:10.1287/serv.2021.0294.
""")
st.markdown("---")

# Pie de página
st.markdown("**Presentación creada con Streamlit por [Tu Nombre]**")


# Pie de página
st.markdown("**Presentación creada con Streamlit por  Juan Esteban Estrada")
