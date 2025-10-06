@echo off
echo ========================================
echo INSTALACION - Trabajo Final Series de Tiempo
echo Universidad de Buenos Aires - IA
echo ========================================
echo.

echo [1/3] Instalando dependencias basicas...
pip install pandas numpy matplotlib seaborn jupyter notebook statsmodels scikit-learn

echo.
echo [2/3] Descargando datos de Bitcoin...
python descargar_datos.py

echo.
echo [3/3] Iniciando Jupyter Notebook...
echo.
echo El navegador se abrira automaticamente.
echo Para detener el servidor, presiona Ctrl+C
echo.

jupyter notebook notebooks/01_analisis_exploratorio.ipynb

pause
