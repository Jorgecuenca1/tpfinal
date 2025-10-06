# 🚀 INSTRUCCIONES DE INICIO - Trabajo Final Series de Tiempo

## ✅ PROYECTO CONFIGURADO EXITOSAMENTE

### 📊 Jupyter Notebook está ejecutándose!

**Accede al notebook a través de cualquiera de estos enlaces:**

🔗 http://localhost:8888/tree?token=1492f8b39b0eebf03bd82e6fe92339b86dda5d1a93724801

🔗 http://127.0.0.1:8888/tree?token=1492f8b39b0eebf03bd82e6fe92339b86dda5d1a93724801

---

## 📁 ARCHIVOS CREADOS

✅ **Estructura del proyecto creada:**
- `data/raw/` - Para datos originales
- `data/processed/` - Para datos procesados
- `notebooks/` - Notebooks de análisis
- `src/` - Código Python
- `reports/` - Informe final

✅ **Archivos principales:**
- `notebooks/01_analisis_exploratorio.ipynb` - **Notebook principal listo para usar**
- `requirements.txt` - Dependencias del proyecto
- `descargar_datos.py` - Script para descargar datos
- `setup.bat` - Instalación automática
- `README.md` - Documentación completa
- `DATASETS_RECOMENDADOS.md` - Fuentes de datos sugeridas
- `CLAUDE.md` - Guía para Claude Code

---

## 🎯 PRÓXIMOS PASOS

### 1. Descargar los datos de Bitcoin

Tienes 3 opciones:

#### Opción A: Script automático (puede fallar por límites de API)
```bash
python descargar_datos.py
```

#### Opción B: Descarga manual desde Yahoo Finance
1. Ir a: https://finance.yahoo.com/quote/BTC-USD/history
2. Seleccionar "Max" en el rango de fechas
3. Clic en "Download"
4. Guardar el archivo como: `data/raw/bitcoin_historical.csv`

#### Opción C: Descarga desde Kaggle (recomendado)
1. Ir a: https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data
2. Descargar el dataset
3. Extraer y copiar a: `data/raw/bitcoin_historical.csv`

### 2. Abrir el Notebook

El notebook ya está abierto en: http://localhost:8888/tree?token=1492f8b39b0eebf03bd82e6fe92339b86dda5d1a93724801

O ejecuta:
```bash
.venv/Scripts/jupyter.exe notebook notebooks/01_analisis_exploratorio.ipynb
```

### 3. Ejecutar el análisis

Una vez tengas los datos:
1. Abre el notebook `01_analisis_exploratorio.ipynb`
2. Ejecuta las celdas una por una (Shift + Enter)
3. El notebook incluye:
   - Carga y limpieza de datos
   - Análisis exploratorio visual
   - Test de estacionariedad
   - Autocorrelación (ACF/PACF)
   - Descomposición de la serie
   - División train/test

---

## 🔧 COMANDOS ÚTILES

### Verificar instalación
```bash
.venv/Scripts/python.exe -c "import pandas; import numpy; import matplotlib; print('OK')"
```

### Instalar dependencias adicionales
```bash
.venv/Scripts/pip.exe install <paquete>
```

### Detener Jupyter Notebook
Presiona `Ctrl + C` dos veces en la terminal donde está corriendo

### Reiniciar Jupyter Notebook
```bash
.venv/Scripts/jupyter.exe notebook notebooks/01_analisis_exploratorio.ipynb
```

---

## 📊 DATASET RECOMENDADO

**Bitcoin Historical Data (2012-2025)**
- **Fuente:** Yahoo Finance / Kaggle
- **URL Kaggle:** https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data
- **Frecuencia:** Diaria (puede agregarse a diferentes niveles)
- **Variables:** Date, Open, High, Low, Close, Volume

**Pregunta de investigación sugerida:**
> "¿Cómo han evolucionado los patrones de volatilidad del Bitcoin desde su creación y qué modelos de series de tiempo predicen mejor sus movimientos de precio a corto y mediano plazo?"

---

## 📚 MODELOS A IMPLEMENTAR (Mínimo 3)

1. **ARIMA/SARIMA** - Modelo estadístico clásico
2. **LSTM** - Red neuronal recurrente (Deep Learning)
3. **Prophet** - Modelo de Facebook para series temporales

---

## 📝 ENTREGABLES

### Código (50%)
- ✅ Limpieza y preparación de datos
- ⏳ Creación de al menos 3 modelos
- ⏳ Generación de pronósticos y evaluación

### Informe (50%)
- ⏳ Pregunta de investigación
- ⏳ Descripción de datos
- ⏳ Descripción de modelos
- ⏳ Pruebas y evaluaciones
- ⏳ Conclusiones

**Fecha límite:** 18 de junio, 7:00 PM

---

## ⚠️ IMPORTANTE

- Todos los archivos deben incluir **códigos y nombres de todos los integrantes**
- El código debe ser **reproducible** (ejecutable)
- Incluir **comentarios** explicativos

---

## 🆘 SOPORTE

Si tienes problemas:

1. **Error al cargar datos:** Verifica que el archivo CSV esté en `data/raw/bitcoin_historical.csv`
2. **Error de librería:** Reinstala con `pip install -r requirements.txt`
3. **Jupyter no inicia:** Verifica que el puerto 8888 no esté en uso
4. **Dudas del proyecto:** Consultar con el docente Camilo Argoty

---

**¡Éxito con el proyecto! 🚀**
