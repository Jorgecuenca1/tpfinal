"""
Script para descargar datos históricos de Bitcoin
Trabajo Final - Análisis de Series de Tiempo - UBA
"""

import urllib.request
import os

def descargar_bitcoin_data():
    """
    Descarga datos históricos de Bitcoin desde Yahoo Finance
    """
    print("Descargando datos historicos de Bitcoin...")

    # URL de datos históricos de Bitcoin desde Yahoo Finance
    # Datos desde 2014 hasta presente
    url = "https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1410912000&period2=9999999999&interval=1d&events=history"

    # Crear directorio si no existe
    os.makedirs('data/raw', exist_ok=True)

    # Ruta de destino
    filepath = 'data/raw/bitcoin_historical.csv'

    try:
        # Descargar archivo
        urllib.request.urlretrieve(url, filepath)
        print(f"OK - Datos descargados exitosamente en: {filepath}")

        # Mostrar primeras líneas
        with open(filepath, 'r') as f:
            lines = f.readlines()[:6]
            print("\nPrimeras lineas del dataset:")
            for line in lines:
                print(line.strip())

        return filepath

    except Exception as e:
        print(f"ERROR al descargar: {e}")
        print("\nAlternativa: Descargar manualmente desde:")
        print("   https://finance.yahoo.com/quote/BTC-USD/history")
        return None

if __name__ == "__main__":
    descargar_bitcoin_data()
