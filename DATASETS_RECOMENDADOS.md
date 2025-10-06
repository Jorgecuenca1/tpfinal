# 📊 Datasets Recomendados para Análisis de Series de Tiempo

## 🏆 TOP 5 DATASETS RECOMENDADOS

### 1. 💰 Bitcoin Historical Data (2012-2025) - **MUY RECOMENDADO**
- **URL**: https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data
- **Actualización**: Actualizado hace 17 horas
- **Descripción**: Datos de Bitcoin a intervalos de 1 minuto desde enero 2012 hasta el presente
- **Pregunta de investigación sugerida**: "¿Cómo han evolucionado los patrones de volatilidad del Bitcoin desde 2012 y qué modelos predicen mejor sus movimientos a corto plazo?"
- **Ventajas**:
  - Datos muy actualizados
  - Alta frecuencia (1 minuto)
  - Ideal para comparar modelos ARIMA, LSTM y Prophet

### 2. 🌍 Calidad del Aire - India (2010-2023)
- **URL**: https://www.kaggle.com/datasets/abhisheksjha/time-series-air-quality-data-of-india-2010-2023
- **Descripción**: Datos históricos de calidad del aire en ciudades de India
- **Pregunta de investigación sugerida**: "¿Es posible predecir niveles peligrosos de contaminación con 48 horas de anticipación para alertar a la población?"
- **Ventajas**:
  - Relevancia social y ambiental
  - Serie temporal larga (13 años)
  - Múltiples variables (PM2.5, PM10, NO2, etc.)

### 3. 🛒 Store Sales - Time Series Forecasting
- **URL**: https://www.kaggle.com/competitions/store-sales-time-series-forecasting
- **Descripción**: Competencia de Kaggle para predecir ventas de tiendas
- **Pregunta de investigación sugerida**: "¿Qué modelo de series de tiempo captura mejor los patrones estacionales y promocionales en ventas minoristas?"
- **Ventajas**:
  - Dataset de competencia (bien estructurado)
  - Incluye variables exógenas (promociones, fechas especiales)
  - Muchos ejemplos de código disponibles

### 4. 📈 Crypto & Stocks Market Data (2025-Presente)
- **URL**: https://www.kaggle.com/datasets/adrianjuliusaluoch/crypto-and-stock-market-data-for-financial-analysis
- **Descripción**: Datos horarios de criptomonedas y acciones, actualizado diariamente
- **Pregunta de investigación sugerida**: "¿Existe correlación entre movimientos de criptomonedas y acciones tradicionales que permita predicción cruzada?"
- **Ventajas**:
  - Muy actual (2025)
  - Múltiples activos
  - Datos horarios

### 5. 🌡️ Daily Climate Time Series Data
- **URL**: https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data
- **Descripción**: Datos climáticos diarios de Delhi (2013-2017)
- **Pregunta de investigación sugerida**: "¿Cómo afecta el cambio climático los patrones de temperatura y pueden predecirse olas de calor?"
- **Ventajas**:
  - Múltiples variables (temperatura, humedad, velocidad del viento, presión)
  - Patrones estacionales claros
  - Datos completos y limpios

---

## 📋 OTROS DATASETS INTERESANTES

### Calidad del Aire (UCI)
- **URL**: https://www.kaggle.com/datasets/fedesoriano/air-quality-data-set
- Respuestas de sensores de óxido metálico, promedios horarios

### Bitcoin & Ethereum (2014-2025)
- **URL**: https://www.kaggle.com/datasets/kapturovalexander/bitcoin-and-ethereum-prices-from-start-to-2023
- Precios diarios de las dos criptomonedas más importantes

### Historical Air Quality (USA - EPA)
- **URL**: https://www.kaggle.com/datasets/epa/epa-historical-air-quality
- Datos de calidad del aire de monitores en todo Estados Unidos

---

## 🎯 RECOMENDACIÓN FINAL

**Para este proyecto, recomiendo el Dataset #1 (Bitcoin Historical Data)** por las siguientes razones:

1. ✅ **Datos actualizados constantemente** - hasta 2025
2. ✅ **Alta frecuencia** - datos por minuto (pueden agregarse a horas/días según necesites)
3. ✅ **Pregunta de investigación interesante** - predicción de precios
4. ✅ **Ideal para comparar modelos**:
   - ARIMA/SARIMA (modelos clásicos estadísticos)
   - LSTM/GRU (deep learning)
   - Prophet (modelo especializado de Facebook)
5. ✅ **Patrones claros** - tendencias, estacionalidad, volatilidad
6. ✅ **Relevancia actual** - criptomonedas son un tema de interés

---

## 📥 CÓMO DESCARGAR

### Opción 1: Interfaz Web
1. Ir a la URL del dataset
2. Hacer clic en "Download" (requiere cuenta de Kaggle - es gratis)
3. Descomprimir el archivo

### Opción 2: Kaggle API (Recomendado para reproducibilidad)
```bash
# Instalar Kaggle API
pip install kaggle

# Configurar credenciales (descargar kaggle.json desde tu perfil de Kaggle)
# Colocar en: C:\Users\HOME\.kaggle\kaggle.json (Windows)

# Descargar dataset (ejemplo Bitcoin)
kaggle datasets download -d mczielinski/bitcoin-historical-data

# Descomprimir
unzip bitcoin-historical-data.zip
```

---

## 📝 ESTRUCTURA SUGERIDA DEL PROYECTO

```
tpfinal/
├── data/
│   ├── raw/              # Datos originales descargados
│   └── processed/        # Datos limpios
├── notebooks/
│   ├── 01_exploracion.ipynb
│   ├── 02_limpieza.ipynb
│   ├── 03_modelo_arima.ipynb
│   ├── 04_modelo_lstm.ipynb
│   ├── 05_modelo_prophet.ipynb
│   └── 06_comparacion.ipynb
├── src/
│   ├── data_processing.py
│   ├── models.py
│   └── evaluation.py
├── reports/
│   └── informe_final.pdf
├── requirements.txt
└── README.md
```
